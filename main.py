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
    record_audio(5, audio_file_path)
    # Transcribe the audio file
    transcription = str(transcribe(audio_file_path)["text"])
    print(f"Transcription: {transcription}")

    # Check the validity of the transcribed text
    validity_result = check_validity(transcription)
    print(validity_result)
    # If there is no key 'True' in the dictionary, it means we have a message explaining why it's False
    if 'True' not in validity_result:
        # It assumes that if 'True' is not a key, then 'False' will be, adjust as per your 'check_validity' function's logic
        false_message = validity_result.get('False', 'The statement is invalid, but no message was provided.')
        speak(false_message)
        print(false_message)
    else:
        speak("The statement is valid.")
        print("The statement is valid.")

if __name__ == "__main__":
    main()


