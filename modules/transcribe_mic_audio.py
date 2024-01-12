"""Sample Python script to transcribe an audio file with AssemblyAI"""
import os

import assemblyai as aai

# Load API key from environment variables
aai.settings.api_key = os.getenv("AAI_API_KEY")


# Define event handling for AssemblyAI streaming events
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


def main():
    transcriber = aai.RealtimeTranscriber(
        sample_rate=16_000,
        on_data=on_data,
        on_error=on_error,
        on_open=on_open,
        on_close=on_close,
    )

    # Connect to AssemblyAI's real-time transcription service via WebSockets
    transcriber.connect()

    # Open up a microphone stream with a sample rate of 16_000
    microphone_stream = aai.extras.MicrophoneStream(sample_rate=16_000)

    # Send microphone stream to transcriber service
    # until end/stop of recording (trigger by Ctrl+C)
    transcriber.stream(microphone_stream)

    # Close the stream to the transcriber
    transcriber.close()

    # Just in case, close the microphone stream as well
    microphone_stream.close()


if __name__ == "__main__":
    main()
