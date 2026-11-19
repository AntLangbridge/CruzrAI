
import os

import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel


SAMPLE_RATE = 16000
DEFAULT_DURATION = 5
MODEL_SIZE = "large-v3"


class SpeechInput:
    def __init__(self):
        self.model = None

    def load_model(self):
        """Load Whisper only when speech recognition is needed."""
        if self.model is None:
            print("Loading Whisper large-v3...")

            self.model = WhisperModel(
                MODEL_SIZE,
                device="cuda",
                compute_type="float16"
            )

            print("Speech recognition ready.")

    def record(self, duration=DEFAULT_DURATION):
        """Record audio from the default microphone."""
        print(f"\nRecording for {duration} seconds...")
        print("Speak now.")

        audio = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32"
        )

        sd.wait()
        return np.asarray(audio).flatten()

    def transcribe(self, audio):
        """Convert recorded speech into text."""
        self.load_model()

        segments, info = self.model.transcribe(
            audio,
            beam_size=5,
            vad_filter=True
        )

        text = " ".join(
            segment.text.strip() for segment in segments
        ).strip()

        if text:
            print(f"Detected language: {info.language}")
            print(f"Transcription: {text}")

        return text

    def listen(self, duration=DEFAULT_DURATION):
        """Record and transcribe one spoken utterance."""
        audio = self.record(duration)
        return self.transcribe(audio)
