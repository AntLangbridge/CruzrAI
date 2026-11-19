
# Cruzr AI — Changelog

All notable changes to the Cruzr AI software project will be documented here.

## [Unreleased]

### Planned
- Implement speech recognition and text-to-speech.
- Improve interpreter accuracy and language selection.
- Introduce accessibility and communication preferences.
- Develop integration with UBTECH Cruzr hardware and ROS.


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