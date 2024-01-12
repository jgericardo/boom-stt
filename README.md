# Speech-to-Text Service

A Speech-to-text transcription service using AssemblyAI.

## Setup

- Python version: `Python 3.11.4`
- Virtual environment (pyenv): `pyenv 2.3.25`
- Poetry: `1.6.1`

If you have PyEnv installed, you may create a virtual environment from the project repo,

```shell
$ pyenv virtualenv 3.11.4 "<your-venv-name>"
$ pyenv local "<your-venv-name>"
```

To install dependencies using Poetry,

```shell
$ poetry install
```

Additional dependencies from AssemblyAI,

```shell
# (Mac)
$ brew install portaudio

# (Debian/Ubuntu)
$ apt install portaudio19-dev
```

To avoid exposing of your API key, add it as an environment variable/secret,

```shell
$ export AAI_API_KEY="<your-API-key>"
```

## Usage

To transcribe an audio file, run the script below

```shell
$ python modules/transcribe_audio_file.py -af "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
```

To transcribe audio from a microphone, run the script below

```shell
# Press Ctrl+C to stop recording
$ python modules/transcribe_mic_audio.py
```
