import pyaudio
import wave
import openai
import pyttsx3
import os
from audio import *
from tts import *
from validity import *

def main():
    audio_file_path = "recording.wav"
    # Record audio and save as WAV file
    record_audio(10, audio_file_path)
    # Transcribe the audio file
    transcription = transcribe(audio_file_path)
    print(f"Transcription: {transcription}")

    # Check the validity of the transcribed text
    validity_result = check_validity(transcription)
    
    # If the result is not True, it means we have a message explaining why it's False
    if validity_result is not True:
        speak(validity_result["False"])
        print(validity_result["False"])
    else:
        speak("The statement is valid.")
        print("The statement is valid.")

if __name__ == "__main__":
    main()

