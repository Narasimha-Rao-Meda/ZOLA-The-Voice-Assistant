import speech_recognition as sr
from speeking_engine import speak

r = sr.Recognizer()

def command():
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise  (source)
        audio = r.listen(source)
    try:
        user_input = r.recognize_google(audio,language='en')
    except:
        speak("Pardon me, can you say that again")
        user_input = command()
    return user_input

        

        