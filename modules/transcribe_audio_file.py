"""Sample Python script to transcribe an audio file with AssemblyAI"""
import argparse
import os
import string

import assemblyai as aai

# Load API key from environment variables
aai.settings.api_key = os.getenv("AAI_API_KEY")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Audio file transcription script with AssemblyAI",
    )
    parser.add_argument(
        "-af",
        "--audio-file",
        help="File path or URL to audio file to transcribe.",
        required=True,
    )
    parsed_args = vars(parser.parse_args())
    return parsed_args


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


def main(args):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(args["audio_file"])
    print(f"Audio file transcription:\n{transcript.text}")
    print(f"\nAnnotated text:\n{annotate_text(transcript.text)}")


if __name__ == "__main__":
    args = parse_args()
    main(args)
