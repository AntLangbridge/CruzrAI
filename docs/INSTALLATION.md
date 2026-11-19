
# Cruzr AI — Installation Guide

## Overview

Cruzr AI is a modular robotics autonomy platform being developed
for the UniSC Robotics Laboratory's UBTECH Cruzr robots.

This guide documents the current Windows development environment.
Installation on Cruzr hardware is not yet supported.

## 1. Development Requirements

### Software
- Windows 10 or 11 (Windows 11 not yet independently tested)
- Python 3.11 or newer
- Git
- Ollama
- NVIDIA graphics driver for GPU acceleration

### Tested Hardware
- NVIDIA GeForce RTX 3090 (24 GB VRAM)

### Tested GPU Libraries
- NVIDIA CUDA Toolkit 12.9
- NVIDIA cuDNN 9.28 for CUDA 12.9

Other configurations may work but have not yet been validated.

## 2. Clone the Repository

Clone the project from GitHub:

    git clone <repository-url>
    cd CruzrAI

Replace `<repository-url>` with the actual GitHub repository URL.

## 3. Create the Python Environment

Open PowerShell in the project folder:

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1

Install the Python dependencies:

    python -m pip install -r requirements.txt

## 4. Install Ollama

Download Ollama:

https://ollama.com/download

Install the configured conversational model:

    ollama pull qwen2.5:7b

Ollama must be running when using the conversational application.

## 5. Configure GPU Speech Recognition

Download and install CUDA 12.9:

https://developer.nvidia.com/cuda-12-9-0-download-archive

Install NVIDIA cuDNN 9 for CUDA 12.9:

https://developer.nvidia.com/cudnn

The tested cuDNN installation used:

    C:\Program Files\NVIDIA\CUDNN\v9.28\bin\12.9\x64

The tested CUDA installation used:

    C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.9\bin

These directories must be accessible through the system PATH
for the tested GPU configuration.

The current development environment required temporary
PowerShell PATH adjustments:

    $env:PATH = "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.9\bin;$env:PATH"
    $env:PATH = "C:\Program Files\NVIDIA\CUDNN\v9.28\bin\12.9\x64;$env:PATH"

These commands affect only the current PowerShell session.

## 6. Test Speech Recognition

Run:

    python test_whisper.py

The first execution may download the configured Whisper model. This takes some time and 
doesn't display a progress bar so be patient with it.

The current reference model is Whisper large-v3.

## 7. Run Cruzr AI

Run:

    python main.py

Available commands:

- /voice — Record and transcribe microphone input.
- /profile — Change operating profile.
- /reset — Clear the current conversation.
- /quit — Exit the application.

Speech recognition currently uses a fixed-duration recording.
Text-to-speech has not yet been implemented.

## 8. Current Limitations

- Development prototype only.
- No direct Cruzr hardware integration.
- No autonomous navigation or mapping integration.
- Campus knowledge coverage is limited.
- GPU speech recognition requires compatible NVIDIA libraries.
- The application has not been validated on other computers.
- University network and security requirements have not
  yet been assessed for deployment.

## 9. Troubleshooting

### Ollama HTTP 400

Check that the configured model exists and that the
application sends a valid request to Ollama.

### Missing cublas64_12.dll

Check that CUDA 12 libraries are installed and accessible
through PATH.

### Missing cuDNN libraries

Check that cuDNN 9 for CUDA 12 is installed and that its
DLL directory is accessible through PATH.

### Microphone not detected

Confirm that Windows microphone permissions are enabled
and that the intended recording device is selected.

## 10. Future Development

Future installation documentation will cover:
- Cross-platform compatibility.
- Robot-specific configuration.
- Cruzr hardware interfaces.
- ROS integration.
- Deployment architecture and remote processing.
