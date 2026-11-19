
from pathlib import Path

import numpy as np
import sounddevice as sd
import soundfile as sf


AUDIO_FILE = Path(
    "recordings/voice_samples/stormy_delta_integration.wav"
)

# Attenuate playback while testing.
MAX_PEAK = 0.15


def main():
    if not AUDIO_FILE.exists():
        raise FileNotFoundError(AUDIO_FILE)

    audio, sample_rate = sf.read(
        str(AUDIO_FILE),
        dtype="float32",
    )

    if audio.size == 0 or not np.isfinite(audio).all():
        raise RuntimeError("Invalid audio recording.")

    peak = float(np.max(np.abs(audio)))

    if peak > MAX_PEAK:
        audio = audio * (MAX_PEAK / peak)

    print(f"Recording: {AUDIO_FILE.name}")
    print(f"Duration: {len(audio) / sample_rate:.2f} seconds")
    print(f"Playback sample rate: {sample_rate} Hz")

    input("Press Enter to play the recording...")

    sd.play(audio, samplerate=sample_rate)
    sd.wait()

    print("Playback completed.")


if __name__ == "__main__":
    main()