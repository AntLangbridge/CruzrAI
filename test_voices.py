
from pathlib import Path
import wave

from piper import PiperVoice, SynthesisConfig


MODEL_PATH = Path("models/tts/en_AU-librivox-medium.onnx")
OUTPUT_DIR = Path("recordings/voice_samples")

TEST_PHRASE = (
    "G'day! I'm Stormy, your friendly campus assistant. "
    "Need a hand finding something?"
)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading Australian Piper voice model...")
    voice = PiperVoice.load(str(MODEL_PATH))

    speaker_count = voice.config.num_speakers
    print(f"Available speakers: {speaker_count}")

    for speaker_id in range(speaker_count):
        output_path = OUTPUT_DIR / f"stormy_voice_{speaker_id:02d}.wav"

        print(f"Generating speaker {speaker_id}...")

        with wave.open(str(output_path), "wb") as wav_file:
            voice.synthesize_wav(
                TEST_PHRASE,
                wav_file,
                SynthesisConfig(speaker_id=speaker_id),
            )

    print(f"\nGenerated {speaker_count} voice samples.")
    print(f"Samples saved to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
