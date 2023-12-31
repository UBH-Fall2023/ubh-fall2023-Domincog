import pyttsx3
from elevenlabs import generate, play, set_api_key
from gtts import gTTS
import os
from playsound import playsound

api_key = ""
set_api_key(api_key)


engine = pyttsx3.init()

#def speak(text):
#    engine.setProperty('rate', 150) 
#    engine.say(text)
#    engine.runAndWait()

def speak(text):
    # Generate the audio using the ElevenLabs API
    audio = generate(
        text=text,
        voice="Liam",  # You can ch0oose the voice you want
        model="eleven_multilingual_v2"  # Or "eleven_monolingual_v1" for English
    )

    # Play the generated audio
    play(audio)
    


def speak_google(text):
    tts = gTTS(text=text, lang='en')
    filename = "file.mp3"
    tts.save(filename)
    playsound(filename)



    

def read_file(filepath):
    with open(filepath) as file:
        text = file.read()
    return text
    
def main():
    # This is where you could read from a file if needed.
    # For example, if you have a file named 'message.txt' with the content "hello world", you could do:
    # message = read_file('message.txt')
       
    # But for now, we will just say "hello world" directly.
    #speak("Joseph Biden lost the 2020 election.")
    speak_google("Joseph Biden lost the 2020 election.")

if __name__ == "__main__":
    main()

