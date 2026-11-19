
from pathlib import Path
import time
import numpy as np
import soundfile as sf
import torch
import sounddevice as sd
import unicodedata
from transformers import AutoModelForCausalLM, AutoTokenizer
from snac import SNAC


MODEL_REPO = "ablmontazer/orpheus-australian-en-tts"
SNAC_REPO = "hubertsiuzdak/snac_24khz"
SAMPLE_RATE = 24000

# Orpheus token identifiers
SOH = 128259
EOT = 128009
EOH = 128260
SOAI = 128261
SOS = 128257
EOAI = 128262
PAD = 128263
BASE_A = 128266

def prepare_speech_text(text):
    """Remove characters unsuitable for spoken output."""
    cleaned = []

    for char in text:
        category = unicodedata.category(char)

        # Remove emoji symbols, formatting controls and
        # other non-spoken characters.
        if category.startswith(("S", "C")):
            continue

        cleaned.append(char)

    return " ".join("".join(cleaned).split())

class SpeechOutput:
    def __init__(self, voice="delta", device="cuda"):
        self.voice = voice.lower()
        self.device = device
        self.tokenizer = None
        self.model = None
        self.decoder = None

    def load_model(self):
        """Load the Orpheus model and SNAC decoder."""
        if self.model is not None:
            return

        if self.device == "cuda" and not torch.cuda.is_available():
            raise RuntimeError(
                "CUDA is unavailable. Orpheus requires GPU "
                "acceleration in the current configuration."
            )

        print("Loading Orpheus speech model...")

        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_REPO)

        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_REPO,
            torch_dtype=torch.bfloat16,
        ).to(self.device).eval()

        print("Loading SNAC audio decoder...")

        self.decoder = SNAC.from_pretrained(
            SNAC_REPO
        ).to(self.device).eval()

        print(f"Speech output ready. Voice: {self.voice}")

    def synthesize(self, text):
        """Generate speech and return audio samples and timing."""
        if not text or not text.strip():
            raise ValueError("Speech text cannot be empty.")

        text = prepare_speech_text(text)

        if not text:
            raise ValueError("No speakable text remains after cleaning.")

        self.load_model()

        input_ids = (
            [SOH]
            + self.tokenizer.encode(
                f"{self.voice}: {text}",
                add_special_tokens=False,
            )
            + [EOT, EOH, SOAI, SOS]
        )

        start = time.perf_counter()

        with torch.inference_mode():
            generated = self.model.generate(
                torch.tensor(
                    [input_ids], device=self.device
                ),
                max_new_tokens=1400,
                do_sample=True,
                temperature=0.6,
                top_p=0.95,
                eos_token_id=EOAI,
                pad_token_id=PAD,
            )[0].tolist()

            audio_tokens = [
                token
                for token in generated[len(input_ids):]
                if BASE_A <= token < BASE_A + 7 * 4096
            ]

            frame_count = len(audio_tokens) // 7

            if frame_count == 0:
                raise RuntimeError(
                    "Orpheus generated no usable audio frames."
                )

            codes_0, codes_1, codes_2 = [], [], []

            for i in range(frame_count):
                frame = [
                    token - BASE_A
                    for token in audio_tokens[i * 7:i * 7 + 7]
                ]

                codes_0.append(frame[0] % 4096)
                codes_1.extend([
                    frame[1] % 4096,
                    frame[4] % 4096,
                ])
                codes_2.extend([
                    frame[2] % 4096,
                    frame[3] % 4096,
                    frame[5] % 4096,
                    frame[6] % 4096,
                ])

            codes = [
                torch.tensor(
                    codes_0, device=self.device
                )[None],
                torch.tensor(
                    codes_1, device=self.device
                )[None],
                torch.tensor(
                    codes_2, device=self.device
                )[None],
            ]

            audio = (
                self.decoder.decode(codes)[0, 0]
                .cpu()
                .numpy()
            )

        elapsed = time.perf_counter() - start

        # Basic validation, not a complete artifact detector.
        if audio.size == 0 or not np.isfinite(audio).all():
            raise RuntimeError(
                "Speech generation produced invalid audio."
            )

        # Reject unusually high output amplitudes.
        peak_amplitude = float(np.max(np.abs(audio)))

        if peak_amplitude > 1.0:
            raise RuntimeError(
                f"Speech generation exceeded safe digital amplitude: "
                f"{peak_amplitude:.3f}"
            )

        return audio, elapsed

    
    def save(self, text, output_path):
        """Generate speech and save it as a WAV file."""
        output_path = Path(output_path)
        output_path.parent.mkdir(
            parents=True, exist_ok=True
        )

        audio, elapsed = self.synthesize(text)

        sf.write(str(output_path), audio, SAMPLE_RATE)

        return {
            "path": str(output_path),
            "voice": self.voice,
            "duration": len(audio) / SAMPLE_RATE,
            "generation_time": elapsed,
        }

    def play_file(self, audio_path, max_peak=0.15, confirm=True):
        """Play an existing recording with optional manual approval."""
        audio_path = Path(audio_path)

        if not audio_path.exists():
            raise FileNotFoundError(audio_path)

        if not 0 < max_peak <= 1.0:
            raise ValueError("max_peak must be between 0 and 1.")

        audio, sample_rate = sf.read(
            str(audio_path),
            dtype="float32",
        )

        if audio.size == 0 or not np.isfinite(audio).all():
            raise RuntimeError("Invalid audio recording.")

        peak = float(np.max(np.abs(audio)))

        if peak > max_peak:
            audio = audio * (max_peak / peak)

        if confirm:
            response = input(
                f"Play recording '{audio_path.name}'? [y/N]: "
            ).strip().lower()

            if response != "y":
                print("Playback cancelled.")
                return False

        sd.play(audio, samplerate=sample_rate)
        sd.wait()

        return True


        audio, elapsed = self.synthesize(text)

        sf.write(str(output_path), audio, SAMPLE_RATE)

        return {
            "path": str(output_path),
            "voice": self.voice,
            "duration": len(audio) / SAMPLE_RATE,
            "generation_time": elapsed,
        }