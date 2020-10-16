from speeking_engine import speak, wait
from greet_me import greet
from user_command import command
import webbrowser
import time
from screenshot import take_screenshot
import datetime
import wikipedia
import random
from taking_picture import picture_is_taking
import psutil
from weather_report import weather
import wolframalpha

speak("Hello Boss, {}, I'm your assistant".format(greet()))
speak("Tell me how can I help you now?")


if __name__ == '__main__':
    while True:
        user_input = command().lower()
        print(user_input)  
        if user_input in ['open gmail','gmail']:
            speak('Opening Gmail')
            webbrowser.open_new_tab('https://gmail.com')
            wait(5)
        elif user_input in ['open youtube', 'youtube']:
            speak('Opening Youtube')
            webbrowser.open_new_tab('https://youtube.com')
            wait(5)
        elif user_input in ['open google','google']:
            speak('opening google')
            webbrowser.open_new_tab('https://google.com')
            wait(5)
        elif user_input in ['open maps','maps']:
            speak("Opening maps")
            webbrowser.open_new_tab('https://www.google.co.in/maps')
            wait(5) 
        elif user_input in ['who are you']:
            speak("I am your personal voice assistant")
            wait(3)
        elif user_input in ['what is your name', "what's your name"]:
            speak('My name is Zola')
            wait(3)
        elif user_input in ['take a screenshot','screenshot']:
            speak("Screenshot is taking")
            take_screenshot()
            speak("Your screenshot stored in Images folder")
            wait(3)
        elif user_input in ['take a picture','capture a picture','take a photo','photo','']:
            speak("Picture is taking smile please")
            picture_is_taking()
            speak("Your photo stored in Images folder")
            wait(2)
        elif user_input in ['Hey Zola','Zola','Hey','are you there']:
            speak("Yes Boss, I am listening")
            wait(1)
        elif user_input in ['date','time','What is the time now', 'what is today']:
            dateTime = datetime.datetime.now()
            if user_input in ['date','what is today']:
                speak('{}'.format(dateTime.strftime("%d %B %Y")))
            elif user_input in ['time','what is the time now']:
                speak('{}'.format(dateTime.strftime('%I %M %p')))
            wait(2)
        elif user_input in ['how are you']:
            replay = ['I am good','I am fine','Pretty Good','I am well']
            rep = random.choice(replay)
            speak(rep)
            speak('How are you?')
            command()
            wait(4)
        elif user_input in ["what's up"]:
            speak("Nothing just doing my thing")
            wait(1)
        elif user_input in ['news','what are some news','give me some news headlines']:
            speak('Here are some news')
            webbrowser.open_new_tab('https://timesofindia.indiatimes.com/home/headlines')
            wait(3)
        elif user_input in ['github', 'open github']:
            speak('Github is opening')
            webbrowser.open_new_tab('https://github.com/')
            wait(3)
        elif user_input in ['stack overflow','open stack overflow']:
            speak('Opening Stack Overflow')
            webbrowser.open_new_tab('https://stackoverflow.com/')
            wait(3)
        elif user_input in ['cpu', 'device stats']:
            battery_percentage = psutil.sensors_battery()[0]
            cpu_usage = psutil.cpu_percent()
            speak("Battery is at {}".format(battery_percentage))
            speak("CPU usage is {}".format(cpu_usage))
            wait(2)
        elif user_input in ['weather report','weather','weather forecast']:
            weather()
            wait(2)
        elif user_input in ['stop','close','bye','nothing','seeyou','abort','terminate']:
            speak('Your Voice assistant is closing')
            break
        else:
            try:
                client = wolframalpha.Client('KLGYQH-QYT7LUTLHY')
                res = client.query(user_input)
                answer = next(res.results).text
                if answer in ['(no data available)']:
                    webbrowser.open_new_tab('https:\\google.com\search?q={}'.format(user_input))
                else:
                    speak(answer)
                    print(answer)
            except:
                try:
                    data = wikipedia.page(user_input)
                    url = data.url
                    content = data.content
                    words = content.split(".")
                    speak(words[0])
                    speak("You can get more details here {}".format(url))
                except:
                    speak("{} results opening in web browser".format(user_input))
                    webbrowser.open_new_tab('https:\\google.com\search?q={}'.format(user_input))
            wait(3)        
