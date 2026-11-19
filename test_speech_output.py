
from robot_config import ROBOT_CONFIG
from speech_output import SpeechOutput


def main():
    robot_name = ROBOT_CONFIG["name"]
    voice = ROBOT_CONFIG["tts_voice"]

    print(f"Testing speech output for {robot_name}")
    print(f"Selected voice: {voice}")

    speech = SpeechOutput(voice=voice)

    result = speech.save(
    text=(
        "Hey there! I'm Shady, one of your campus assistants. "
        "What can I help you with today?"
    ),
    output_path="recordings/voice_samples/shady_angus_integration.wav",
)

    print("\nSpeech generation successful!")
    print(f"Voice: {result['voice']}")
    print(f"Audio duration: {result['duration']:.2f} seconds")
    print(f"Generation time: {result['generation_time']:.2f} seconds")
    print(f"Saved to: {result['path']}")


if __name__ == "__main__":
    main()