import pyttsx3


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def read_file(filepath):
    with open(filepath) as file:
        text = file.read()
    return text