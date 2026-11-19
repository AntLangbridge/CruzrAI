
# Cruzr AI

**An independent, modular AI and autonomy platform for UBTECH Cruzr service robots.**

**Status:** Early development | **Version:** v0.3.0 (in development)

## Project Overview

Cruzr AI is a robotics software project developed within the University of the Sunshine Coast (UniSC) Robotics Laboratory.

Its purpose is to create a unified platform for conversational artificial intelligence, speech interaction, environmental perception, mapping, navigation and robot control, reducing reliance on proprietary UBTECH application services.

The primary objective is to develop an **autonomous library assistant** for the UniSC Moreton Bay campus, capable of assisting students with library and academic inquiries while navigating designated library areas.

The project is being developed initially for two UBTECH Cruzr robots, Stormy and Shady.

## Current Capabilities

The following functionality has been implemented and demonstrated on a Windows development computer:

- Locally hosted conversational AI using Ollama and Qwen 2.5 7B.
- Configurable robot identity, initially set to Stormy.
- Library Assistant, Open Day Guide and experimental Interpreter profiles.
- Session-based conversational context and profile switching.
- Initial UniSC Moreton Bay campus information lookup.
- Basic safeguards against fabricated campus directions.
- GPU-accelerated speech recognition using faster-whisper and Whisper large-v3.
- Microphone-based interaction using the `/voice` command.
- Keyboard-based interaction as an alternative.

**Current limitation:** Cruzr AI has not yet been integrated with physical Cruzr hardware. Speech responses, mapping and autonomous navigation are still under development.

## Planned Capabilities

- Natural Australian text-to-speech.
- Multilingual speech interaction and translation.
- Accessible communication interfaces.
- ROS-based hardware integration.
- Environmental mapping and localisation.
- Obstacle detection and autonomous navigation.
- Library assistance and approved campus wayfinding.
- Multi-robot operation and configurable deployment profiles.

## Development Milestones

| Milestone | Description | Status |
|---|---|---|
| M1 | Conversational AI with reliable campus information | In progress |
| M2 | Voice interaction and basic robot integration | In progress |
| M3 | Supervised autonomous navigation | Planned |
| M4 | Integrated autonomous library assistant | Planned |

## Getting Started

For development environment requirements and setup instructions, see:

**[Installation Guide](docs/INSTALLATION.md)**

Once installed, run:

```powershell
python main.py
```

Available commands:

| Command | Function |
|---|---|
| `/voice` | Record a spoken question and transcribe it |
| `/profile` | Switch operating profiles |
| `/reset` | Clear conversation history |
| `/quit` | Exit Cruzr AI |

## Project Structure

```text
CruzrAI/
├── main.py
├── profiles.py
├── robot_config.py
├── campus_knowledge.py
├── campus_data.json
├── speech_input.py
├── test_whisper.py
├── requirements.txt
├── CHANGELOG.md
├── README.md
├── requirements.txt
├── .gitignore
└── docs/
    └── INSTALLATION.md
```

## Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Changelog](CHANGELOG.md)

Project management, development progress and WIL documentation are maintained separately within UniSC's Robotics CoLab SharePoint environment.

## Development and Contributions

Cruzr AI is currently under active development.

The long-term intention is to make suitable components available for educational, research and open-source collaboration, subject to university approval and applicable intellectual-property requirements.

No open-source licence has yet been selected.

## Disclaimer

Cruzr AI is an experimental research and development project.

It is not presently validated for unsupervised operation, safety-critical navigation, access to private student records or professional interpreting services.

UBTECH Cruzr is a product of UBTECH Robotics. This project is an independent development initiative and is not an official UBTECH software release.