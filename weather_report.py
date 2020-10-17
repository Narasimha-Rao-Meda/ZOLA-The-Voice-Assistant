import requests
from speeking_engine import speak
from user_command import command

def weather():
    speak("What is the city name?")
    city = command()
    #api_key for open weather map
    api_key = 'your api_key'
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        temperature = ((temperature-273)*1.8)+2
        temperature = (temperature-32)*5/9
        humidity = main['humidity']
        wind_speed = data['wind']['speed']
        report = data['weather']
        speak("Temperature is {:.2f} degree Celsius".format(temperature))
        speak("Humidity is {} percent".format(humidity))
        speak("Wind Speed is {} miles per second".format(wind_speed))
        speak("Report is {} ".format(report[0]['description']))
    else:
        speak("City not found")
    
