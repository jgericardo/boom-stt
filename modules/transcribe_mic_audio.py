"""Sample Python script to transcribe an audio file with AssemblyAI"""
import os

import assemblyai as aai

# Load API key from environment variables
aai.settings.api_key = os.getenv("AAI_API_KEY")


def on_open(session_opened: aai.RealtimeSessionOpened):
    print("Session ID:", session_opened.session_id)


def on_data(transcript: aai.RealtimeTranscript):
    if not transcript.text:
        return

    if isinstance(transcript, aai.RealtimeFinalTranscript):
        print(transcript.text, end="\r\n")
    else:
        print(transcript.text, end="\r")


def on_error(error: aai.RealtimeError):
    print("An error occured:", error)


def on_close():
    print("Closing Session")


def main(args):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(args["audio_file"])
    print(f"Mic audio transcription:\n{transcript.text}")


if __name__ == "__main__":
    main()
