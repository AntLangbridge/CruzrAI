
# Cruzr AI — Changelog

All notable changes to the Cruzr AI software project will be documented here.

## [Unreleased]

### Added
- Installed `faster-whisper`, `sounddevice` and `numpy` in a Python virtual environment.
- Created `test_whisper.py` for standalone microphone recording and speech recognition.
- Configured GPU-accelerated Whisper inference using an NVIDIA RTX 3090, CUDA 12.9 and cuDNN 9.28.
- Tested Whisper `small` and `large-v3` models.
- Successfully transcribed an Australian English test phrase using Whisper `large-v3`.
- Added reusable `speech_input.py` module using Whisper large-v3.
- Integrated speech recognition into the main application through the `/voice` command.
- Successfully demonstrated spoken input, accurate transcription and campus-information response.
- Preserved keyboard input as an alternative interaction method.
- Initial local Orpheus TTS prototype using the Australian English model and SNAC audio decoding.
- Robot-specific voice configuration: Delta for Stormy and Angus for Shady.
- Reusable `speech_output.py` module for local Australian Orpheus TTS and SNAC audio decoding.
- Configuration-driven voice selection using `robot_config.py`.
- `test_speech_output.py` for standalone TTS integration testing.
- Basic audio validation for empty, non-finite and out-of-range audio samples.
- Controlled WAV playback through `SpeechOutput.play_file()` using the existing sounddevice audio backend.
- Manual playback approval and cancellation.
- Playback peak-amplitude attenuation for initial testing.
- Integrated Orpheus speech output into the main conversational interface through the `/speak` command.
- Support for speaking both verified campus knowledge responses and Ollama-generated conversational replies.
- Speech-text sanitisation to remove most unsupported symbols and emojis before text-to-speech generation.
- Explicit user approval before generated audio playback.

### Changed
- Selected Orpheus TTS over Piper following voice-quality testing.

### Fixed
- Corrected an indentation error in `speech_output.py` that prevented `SpeechOutput.save()` from returning its result.
- Resolved unwanted emoji pronunciation in generated speech.

### Testing
- Confirmed microphone audio capture at 16 kHz.
- Confirmed CUDA GPU detection and FP16 support.
- Verified successful GPU inference after configuring CUDA and cuDNN libraries.
- Observed improved recognition of Australian English and the robot name "Stormy" with `large-v3`.

### Known Limitations
- Speech input requires the `/voice` command; continuous hands-free conversation has not yet been implemented.
- Text-to-speech requires the `/speak` command and manual playback approval.
- Speech generation currently takes approximately 12 seconds for tested short responses, with longer responses taking additional time.
- Generated audio can occasionally contain pronunciation, prosody or severe distortion artifacts.
- Audio validation does not yet reliably detect corrupted speech.
- CUDA and cuDNN paths are currently configured manually in the PowerShell session.

### Planned
- Complete microphone-to-spoken-response integration testing.
- Develop continuous spoken conversation without manual commands.
- Investigate streaming TTS and faster Orpheus inference.
- Improve audio validation and playback safety.
- Introduce configurable microphone and audio settings.
- Improve multilingual interpretation and language selection.
- Introduce accessibility and communication preferences.
- Integrate the AI system with Cruzr hardware and ROS.
- Develop supervised navigation and mapping for library assistance.
- Investigate personality fine-tuning using QLoRA and preference optimisation.

### Development Notes
- Validated Delta's short conversational speech on an RTX 3090.
- Baseline inference throughput: approximately 41 tokens/second.
- Identified occasional pronunciation instability and corrupted audio generation requiring safeguards.
- Identified streaming synthesis and inference optimization as future development priorities.
- Verified Stormy's Delta voice through the reusable TTS module: 11.65-second generation time, with minor speech oscillation.
- Verified Shady's Angus voice through the same module: 12.46-second generation time, with minor word-spacing issues.
- Both voices considered acceptable for initial prototyping.
- Verified both approved playback and cancellation.
- Confirmed playback through the Windows default audio output.
- Automatic playback remains disabled because the current signal checks do not reliably detect speech-generation artifacts.
- Verified campus knowledge → Orpheus → approved playback.
- Verified Ollama → Orpheus → approved playback.
- Identified slow speech generation, occasional prosody issues, and incomplete detection of corrupted audio as outstanding work.
- Identified Qwen2.5's limited humour and conversational style as candidates for future personality fine-tuning.
- Full microphone-to-spoken-response integration remains to be tested.


## [0.2.0] — 2026-11-19

### Added
- Modular personality configuration in `profiles.py`.
- Refined Library Assistant, Open Day Guide and Interpreter profiles.
- Robot identity configuration in `robot_config.py`, initially configured for Stormy.
- Initial UniSC Moreton Bay knowledge base in `campus_data.json`.
- Campus information lookup and fallback handling in `campus_knowledge.py`.
- Configurable Ollama response temperature and token limit.

### Changed
- Increased conversational model temperature to 0.65.
- Introduced a 180-token response limit to encourage shorter replies.
- Improved conversational personality instructions and Australian English handling.
- Updated response labels to use the configured robot name.
- Added explicit robot identity instructions to the conversational AI.

### Fixed
- Incorrect indentation preventing campus knowledge lookup execution.
- Invalid Ollama API request causing HTTP 400 errors.

### Testing
- Confirmed local conversational AI operation after correcting the API request.
- Verified Student Central and library location lookups.
- Confirmed unknown robotics demonstration and room locations return safe fallback responses in tested cases.
- Confirmed the configured Stormy identity is recognised in a conversational test.
- Verified that ordinary conversational questions continue to reach Ollama.

### Known Limitations
- Text-only interaction; speech processing is not yet implemented.
- Campus information is limited to a small initial dataset.
- Campus lookup uses basic keyword matching and may miss unfamiliar phrasing.
- Information safeguards are not yet comprehensive.
- No live university information-system integration.
- Interpreter translation accuracy requires further development.
- No direct Cruzr hardware or ROS integration.


## [0.1.0] — 2026-11-16

### Added
- Initial Python-based conversational AI prototype.
- Local Ollama integration using Qwen 2.5 7B.
- Three selectable operating profiles:
  - Library Assistant
  - Open Day Guide
  - Multilingual Interpreter
- Session-based conversation history.
- Profile switching and conversation reset commands.

### Testing
- Successfully generated conversational responses.
- Confirmed personality profiles could be switched.
- Tested English-to-Mandarin translation.
- Identified weaknesses in Tagalog translation.
- Identified overly verbose responses and generic personality behaviour.

### Known Limitations
- Text-only interaction.
- No connection to Cruzr robot hardware.
- No verified university knowledge database.
- Interpreter accuracy requires further validation.
- No persistent configuration or accessibility settings.