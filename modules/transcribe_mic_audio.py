"""Sample Python script to transcribe an audio file with AssemblyAI"""
import os

import assemblyai as aai

# Load API key from environment variables
aai.settings.api_key = os.getenv("AAI_API_KEY")


def main(args):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(args["audio_file"])
    print(f"Mic audio transcription:\n{transcript.text}")


if __name__ == "__main__":
    main()
