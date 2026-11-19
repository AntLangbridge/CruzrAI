
from pathlib import Path
import time

import torch
import soundfile as sf
from transformers import AutoModelForCausalLM, AutoTokenizer
from snac import SNAC

REPO = "ablmontazer/orpheus-australian-en-tts"
DEVICE = "cuda"

VOICE = "delta"
TEXT = (
    "Hey there! I'm Stormy, your friendly university library assistant. "
    "Need a hand finding something?"
)

OUTPUT = Path("recordings/voice_samples/stormy_delta_test4.wav")

# Orpheus audio/control token IDs
SOH = 128259
EOT = 128009
EOH = 128260
SOAI = 128261
SOS = 128257
EOAI = 128262
PAD = 128263
BASE_A = 128266


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    print("Loading Australian Orpheus model...")
    tokenizer = AutoTokenizer.from_pretrained(REPO)

    model = AutoModelForCausalLM.from_pretrained(
        REPO,
        torch_dtype=torch.bfloat16,
    ).to(DEVICE).eval()

    print(
        "Orpheus attention implementation:",
        model.config._attn_implementation,
)

    print("Loading SNAC audio decoder...")
    decoder = SNAC.from_pretrained(
        "hubertsiuzdak/snac_24khz"
    ).to(DEVICE).eval()

    print(f"\nGenerating {VOICE} voice...")
    start = time.perf_counter()

    input_ids = (
        [SOH]
        + tokenizer.encode(
            f"{VOICE}: {TEXT}",
            add_special_tokens=False,
        )
        + [EOT, EOH, SOAI, SOS]
    )

    generation_start = time.perf_counter()

    with torch.inference_mode():
        generated = model.generate(
            torch.tensor([input_ids], device=DEVICE),
            max_new_tokens=1400,
            do_sample=True,
            temperature=0.6,
            top_p=0.95,
            eos_token_id=EOAI,
            pad_token_id=PAD,
        )[0].tolist()

        print(
        f"Token generation time: "
        f"{time.perf_counter() - generation_start:.2f} seconds"
)

        print(
            "Generated tokens:",
            len(generated) - len(input_ids),
)

        audio_tokens = [
            token for token in generated[len(input_ids):]
            if BASE_A <= token < BASE_A + 7 * 4096
        ]

        frame_count = len(audio_tokens) // 7

        if frame_count == 0:
            raise RuntimeError("No audio tokens generated.")

        codes_0, codes_1, codes_2 = [], [], []

        for i in range(frame_count):
            frame = [
                token - BASE_A
                for token in audio_tokens[i * 7:i * 7 + 7]
            ]

            codes_0.append(frame[0] % 4096)
            codes_1.extend([frame[1] % 4096, frame[4] % 4096])
            codes_2.extend([
                frame[2] % 4096,
                frame[3] % 4096,
                frame[5] % 4096,
                frame[6] % 4096,
            ])

        codes = [
            torch.tensor(codes_0, device=DEVICE)[None],
            torch.tensor(codes_1, device=DEVICE)[None],
            torch.tensor(codes_2, device=DEVICE)[None],
        ]

        audio = decoder.decode(codes)[0, 0].cpu().numpy()

    sf.write(str(OUTPUT), audio, 24000)

    elapsed = time.perf_counter() - start

    print(f"\nVoice sample saved: {OUTPUT}")
    print(f"Audio duration: {len(audio) / 24000:.1f} seconds")
    print(f"Generation time: {elapsed:.1f} seconds")


if __name__ == "__main__":
    main()