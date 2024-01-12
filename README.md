# Speech-to-Text Service

A Speech-to-text transcription service using AssemblyAI.

## Setup

To install dependencies using Poetry,

```shell
poetry install
```

Additional dependencies from AssemblyAI,

```shell
# (Mac)
brew install portaudio

# (Debian/Ubuntu)
apt install portaudio19-dev
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
