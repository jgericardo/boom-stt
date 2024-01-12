"""Sample Python script to transcribe an audio file with AssemblyAI"""
import os
import string

import assemblyai as aai

# Load API key from environment variables
aai.settings.api_key = os.getenv("AAI_API_KEY")


# Define event handling for AssemblyAI streaming events
def on_open(session_opened: aai.RealtimeSessionOpened):
    print("Session ID:", session_opened.session_id)


def on_data(transcript: aai.RealtimeTranscript):
    if not transcript.text:
        return

    transcribed_text = transcript.text
    annotated_text = annotate_text(transcribed_text)
    if isinstance(transcript, aai.RealtimeFinalTranscript):
        print(f"Transcribed text:\n{transcribed_text}", end="\r\n")
        print(f"Annotated text:\n{annotated_text}", end="\r\n")
    else:
        print(f"Transcribed text:\n{transcribed_text}", end="\r")
        print(f"Annotated text:\n{annotated_text}", end="\r")


def on_error(error: aai.RealtimeError):
    print("An error occured:", error)


def on_close():
    print("Closing Session")


# Annotation methods
def annotate_word(word: str) -> str:
    """
    Appends a "-v" suffix if the word or token's alphabet
    character ends with a vowel. Otherwise, append word with a "-c" suffix.

    Parameter
    ---------
    word: str
        Input word to annotate

    Returns
    -------
    annotated_word: str
        Annotated word with either a "-v" or "-c" suffix
    """
    # Define vowel set
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

    # Remove any punctuation character
    translator = str.maketrans("", "", string.punctuation)
    cleaned_word = word.translate(translator)

    # Annotate word based on its last alphabet character
    if cleaned_word.endswith(vowels):
        annotated_word = word + "-v"
        return annotated_word
    else:
        annotated_word = word + "-c"
        return annotated_word


def annotate_text(text: str) -> str:
    """
    Annotates every word or token in a transcription/text.

    Parameter
    ---------
    text: str
        Input text to annotate

    Returns
    -------
    annotated_text: str
        Annotated texts
    """
    tokens = text.split()
    annotated_tokens = list(map(lambda token: annotate_word(token), tokens))
    annotated_text = " ".join(annotated_tokens)
    return annotated_text


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
