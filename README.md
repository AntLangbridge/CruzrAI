
# Cruzr AI

**An independent, modular AI and autonomy platform for UBTECH Cruzr service robots.**

**Status:** Early development | **Version:** v0.3.0 (in development)

## Project Overview

Cruzr AI is a robotics software project developed within the University of the Sunshine Coast (UniSC) Robotics Laboratory.

Its purpose is to create a unified platform for conversational artificial intelligence, speech interaction, environmental perception, mapping, navigation and robot control, reducing reliance on proprietary UBTECH application services.

The primary objective is to develop an **autonomous library assistant** for the UniSC Moreton Bay campus, capable of assisting students with library and academic inquiries while navigating designated library areas.

The project is being developed initially for two UBTECH Cruzr robots, Stormy and Shady.

## Current Capabilities

The following functionality has been implemented and demonstrated
on a Windows development computer:

- Locally hosted conversational AI using Ollama and Qwen2.5 7B.
- Configurable robot identity, initially set to Stormy.
- Library Assistant, Open Day Guide and experimental Interpreter profiles.
- Session-based conversation history and profile switching.
- Verified UniSC Moreton Bay campus information lookup.
- Basic safeguards against fabricated campus directions.
- GPU-accelerated speech recognition using Whisper large-v3.
- Microphone interaction through the `/voice` command.
- Australian text-to-speech using the Orpheus TTS model.
- Distinct prototype voices: Delta (Stormy) and Angus (Shady).
- Speech generation from campus knowledge and Ollama responses.
- Controlled audio playback with manual approval.
- Basic speech-text sanitisation and audio signal validation.
- Keyboard interaction as an accessible alternative.

**Milestone 1 — Conversational Intelligence: Completed (local prototype).**

**Current limitations:** Speech input and output require separate commands. Continuous hands-free interaction, physical Cruzr hardware
integration, mapping and autonomous navigation are not yet implemented. Speech generation also requires further latency and reliability improvements.

## Planned Capabilities

- Continuous, natural spoken conversation without manual commands.
- Streaming text-to-speech and improved response latency.
- Reliable audio validation and conversational interruption handling.
- Multilingual speech interaction and translation.
- Accessible communication interfaces and user preferences.
- ROS-based Cruzr hardware integration and robot behaviours.
- Environmental mapping, localisation and obstacle avoidance.
- Supervised autonomous navigation and approved library wayfinding.
- Multi-robot operation and configurable deployment profiles.
- Personality fine-tuning using methods such as QLoRA and preference optimisation.

## Development Milestones

| Milestone | Description | Status |
|---|---|---|
| M1 | Conversational AI with verified campus information | Completed — local prototype |
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
| `/voice` | Record a spoken question using Whisper and submit it to Cruzr AI |
| `/speak` | Generate speech from the latest response using Orpheus, with manual playback approval |
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
├── speech_output.py
├── test_whisper.py
├── test_orpheus.py
├── test_voices.py
├── test_speech_output.py
├── test_playback.py
├── requirements.txt
├── CHANGELOG.md
├── README.md
├── .gitignore
├── docs/
│   └── INSTALLATION.md
├── models/              # Local downloaded models (Git-ignored)
└── recordings/          # Generated audio files (Git-ignored)

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