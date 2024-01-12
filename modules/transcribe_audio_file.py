"""Sample Python script to transcribe an audio file with AssemblyAI"""
import argparse
import os

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


def main(args):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(args["audio_file"])
    print(f"Audio file transcription:\n{transcript.text}")


if __name__ == "__main__":
    args = parse_args()
    main(args)
