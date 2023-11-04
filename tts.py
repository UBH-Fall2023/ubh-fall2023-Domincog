import pyttsx3


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def read_file(filepath):
    with open(filepath) as file:
        text = file.read()
    return text
    
def main():
    # This is where you could read from a file if needed.
    # For example, if you have a file named 'message.txt' with the content "hello world", you could do:
    # message = read_file('message.txt')
    
    # But for now, we will just say "hello world" directly.
    speak("Hello world! If you can hear this the tts.py file is working properly!")

if __name__ == "__main__":
    main()

