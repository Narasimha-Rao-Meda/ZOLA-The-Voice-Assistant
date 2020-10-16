import pyttsx3
import time

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wait(x):
    time.sleep(x)
    engine.say('I am waiting for your next command')
    print('I am waiting for your next command')
    engine.runAndWait()
    