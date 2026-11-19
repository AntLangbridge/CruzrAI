
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

Open PowerShell in the project directory.

Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Confirm that Python is running from the project environment:

```powershell
python -c "import sys; print(sys.executable)"
```

### Install CUDA-enabled PyTorch

The tested development environment uses PyTorch 2.11.0
with CUDA 12.8 support.

Install the matching GPU-enabled build:

```powershell
python -m pip install torch==2.11.0+cu128 --index-url https://download.pytorch.org/whl/cu128
```

Verify GPU detection:

```powershell
python -c "import torch; print(torch.__version__); print('CUDA available:', torch.cuda.is_available()); print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'Not detected')"
```

The tested system reports an NVIDIA GeForce RTX 3090.

### Install remaining Python dependencies

```powershell
python -m pip install -r requirements.txt
```

The requirements file records the tested Python environment,
including the CUDA-enabled PyTorch version.

PyTorch CUDA wheel availability and installation procedures
may differ on other operating systems or Python versions.

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

## 7. Configure Australian Text-to-Speech

Cruzr AI uses the Australian Orpheus TTS model for locally
generated speech, with SNAC for audio decoding.

Selected prototype voices:
- Stormy: Delta (female)
- Shady: Angus (male)

### Verify PyTorch GPU support

Run:

    python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'Not detected')"

CUDA availability must report True for the tested Orpheus
configuration.

### Download and test the speech model

The Australian Orpheus model is hosted at:

https://huggingface.co/ablmontazer/orpheus-australian-en-tts

The SNAC decoder is hosted at:

https://huggingface.co/hubertsiuzdak/snac_24khz

The models download automatically through Hugging Face
when speech synthesis is first requested.

The initial download requires an internet connection and
several gigabytes of available storage. Subsequent runs
can use cached model files.

### Test speech synthesis

From the project directory, run:

    python test_speech_output.py

The test generates a WAV recording using the voice
specified in robot_config.py.

Generated recordings are stored in the recordings/
directory, which is excluded from Git version control.

### Playback safety

The current prototype requires explicit approval before
playing generated audio.

Basic checks reject empty, non-finite and out-of-range
audio samples, but cannot reliably detect severe audible
distortion or pronunciation artifacts.

Automatic unattended playback is not yet supported.

## 8. Run Cruzr AI

Start Ollama and ensure the configured Qwen2.5 model
is available.

From the activated Python virtual environment, run:

    python main.py

### Available Commands

- `/voice` — Record microphone input, transcribe it using Whisper and submit it to the conversational system.
- `/speak` — Generate speech from the latest response using Orpheus TTS, then request approval before playback.
- `/profile` — Change the active operating profile.
- `/reset` — Clear the current conversation.
- `/quit` — Exit the application.

### Example Interaction

    [library] You: Where is the library?

    Stormy: The Moreton Bay library is in Building A1.
    I don't have verified step-by-step directions yet.

    [library] You: /speak

    Generating speech. This may take a moment...

    Speech generated in 12.00 seconds.
    Recording saved: recordings/latest_response.wav

    Play recording 'latest_response.wav'? [y/N]:

The generation time shown above is illustrative and
varies with response length and hardware performance.

### Current Interaction Behaviour

Microphone input and speech output currently operate
through separate commands.

The system does not yet provide continuous hands-free
conversation, wake-word activation or interruption handling.

Generated speech requires manual playback approval while
audio reliability and safety measures are under development.


## 9. Current Limitations

- Development prototype only; not yet deployed on Cruzr hardware.
- Voice input and output require separate user commands.
- Continuous conversation, wake-word detection and speech interruption handling have not been implemented.
- Orpheus speech generation currently introduces noticeable latency, approximately 12 seconds for tested short responses.
- Generated speech may contain unnatural pronunciation, prosody or severe audio artifacts.
- Basic audio validation does not reliably detect all corrupted recordings; unattended playback remains disabled.
- Robot-specific configuration is preliminary; Stormy is currently the default configured robot.
- No ROS navigation, mapping or physical robot control integration has been implemented.
- Campus knowledge coverage is limited.
- GPU speech recognition requires compatible NVIDIA libraries.
- The complete application has not been validated on another development computer.
- University network, security and deployment requirements have not yet been assessed.

## 10. Troubleshooting

### Ollama HTTP 400

Check that the configured model exists and that the application sends a valid request to Ollama.

### Missing cublas64_12.dll

Check that CUDA 12 libraries are installed and accessible through PATH.

### Missing cuDNN libraries

Check that cuDNN 9 for CUDA 12 is installed and that its DLL directory is accessible through PATH.

### Microphone not detected

Confirm that Windows microphone permissions are enabled and that the intended recording device is selected.

### PyTorch CUDA unavailable

Verify that the CUDA-enabled PyTorch build is installed, rather than the CPU-only version.

Check the installed build:

    python -c "import torch; print(torch.__version__); print(torch.version.cuda); print(torch.cuda.is_available())"

The tested environment uses PyTorch 2.11.0+cu128.

### Orpheus model download or loading failure

Confirm that an internet connection is available for the initial Hugging Face model downloads.

Check available disk space and confirm that the Python environment contains the transformers and snac packages.

### Distorted or unnatural speech

Orpheus may occasionally generate pronunciation errors, unnatural timing or severely distorted audio.

Do not increase playback volume to compensate for distorted recordings.

Regenerate the response or try a shorter sentence. Automatic playback should remain disabled until stronger audio validation has been implemented.

## 11. Future Development

Future installation and deployment documentation will cover:

- Cross-platform compatibility and reproducible environments.
- Robot-specific configuration for Stormy, Shady and other Cruzr platforms.
- Cruzr hardware interfaces and ROS integration.
- Deployment architecture and remote AI processing.
- Continuous spoken interaction and wake-word detection.
- Streaming text-to-speech and inference optimisation.
- Improved audio validation and interruption handling.
- Multilingual speech recognition, translation and synthesis.
- Accessibility and personalised communication settings.
- Deployment of fine-tuned conversational AI models, including potential QLoRA and preference-optimised variants.
