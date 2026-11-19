
import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
DURATION = 5

print("Loading Whisper on GPU...")

model = WhisperModel(
    "large-v3",
    device="cuda",
    compute_type="float16"
)

print(f"\nRecording for {DURATION} seconds...")
print("Speak naturally into your microphone.")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32"
)

sd.wait()

print("\nRecording complete. Transcribing...")

segments, info = model.transcribe(
    audio.flatten(),
    beam_size=5,
    vad_filter=True
)

# Transcription happens as we iterate through the segments.
transcription = " ".join(
    segment.text.strip() for segment in segments
)

print(f"\nDetected language: {info.language}")
print(f"Language confidence: {info.language_probability:.2f}")
print(f"Transcription: {transcription or '[No speech detected]'}")

print("\nGPU transcription test complete.")

