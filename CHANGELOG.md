
# Cruzr AI — Changelog

All notable changes to the Cruzr AI software project will be documented here.

## [Unreleased]

### Planned
- Implement speech recognition and text-to-speech.
- Improve interpreter accuracy and language selection.
- Introduce accessibility and communication preferences.
- Develop integration with UBTECH Cruzr hardware and ROS.

## [0.2.0] — 2026-11-16

### Added
- Separate `profiles.py` configuration module.
- Updated personality instructions for Library Assistant, Open Day Guide and Interpreter profiles.

### Changed
- Increased language-model temperature to 0.65.
- Introduced a 180-token response limit to encourage shorter conversations.

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