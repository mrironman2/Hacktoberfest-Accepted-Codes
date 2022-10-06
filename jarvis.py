# Required Packages -->

from json.tool import main
from time import time
import pyttsx3
import speech_recognition as sr
import pyaudio
import requests
import time
import wikipedia
import webbrowser
import subprocess
import datetime
import random
import os
import pyjokes
import json

# Setting Up Voice Engine -->

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class AI:
    # instance attributes
    def __init__(self, name = "AI", age = 12):
        self.name = name
        self.age = age

    def take(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening")
                speak("Listening")
                audio = r.listen(source, timeout=3)
                r.pause_threshold = 1

                # Make Jarvis Recognize -->

                print("Recognizing")
                query = r.recognize_google(audio, language='en-in')
                query = query.lower()

        except Exception as e:
            print(e)
        return query

class AI_Features(AI):

    def __init__(self, name="AI", age=12):
        super().__init__(name, age)




    def wikipedia_func(self , query_wiki):
        try:
            speak("Searching wikipedia ")
            time.sleep(1)
            real_query = real_query.replace("wikipedia", "")
            result = wikipedia.summary(query_wiki, sentences=2)
            speak(f"According to wikipedia {result}")
        except:
            speak(f"No result on wikipedia found about ,{query_wiki}")

    def rolldice(self):
        roll = [1, 2, 3, 4, 5, 6]
        res = random.choice(roll)
        speak("Rolling The Dice ")
        time.sleep(1)
        speak("Dice is Rolling")
        speak("The Number is {res}")

    def flipcoin(self):
        flip = ["Heads", "Tails"]
        flipr = random.choice(flip)
        speak("flipping coin")
        time.sleep(1)
        speak("It's a {flipr}")

    def weather(self):
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

        querystring = {"lat": "22.7196", "lon": "75.8577"}

        headers = {
            "X-RapidAPI-Key": "hehe get ur own key from below link ",
            "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        resp = response.text
        var1 = json.loads(resp)
        city_name = var1['city_name']
        ct = var1['data'][0]['weather']
        w_info = ct['description']
        print(f"City ,{city_name} , Weather , {w_info} ")
        speak(f"City ,{city_name} , Weather , {w_info} ")

    def temprature(self):
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

        querystring = {"lat": "22.7196", "lon": "75.8577"}

        headers = {
            "X-RapidAPI-Key": "hehe get ur own key from below link ",
            "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        resp = response.text
        var1 = json.loads(resp)
        city_name = var1['city_name']
        ct = var1['data'][0]['app_temp']
        print(f"Current Temprature , {ct} ")
        speak(f"Current Temprature , {ct} ")

    def insult(self):
        insult = requests.get(
            'https://evilinsult.com/generate_insult.php?lang=en&type=json')
        if insult.status_code == 200:
            insult = insult.json()['insult']
            speak(insult)
        else:
            insult = requests.get(
                'https://evilinsult.com/generate_insult.php?lang=en&type=json')
            if insult.status_code == 200:
                insult = insult.json()['insult']
                speak(insult)

    def greeting(self):
        now = datetime.datetime.now()
        hour = now.hour

        if hour < 10:
            greeting = "Good morning"
        elif hour < 17:
            greeting = "Good afternoon"
        elif hour < 20:
            greeting = "Good evening"
        else:
            greeting = "Good night"

        return greeting





if __name__ == "__main__":
    jarvis = AI_Features("Jarvis" , 18)
    greeting = jarvis.greeting()
    speak(f"Hello Master ! {greeting} , What Can I do For You ?")

    try:
        while True:
            query = jarvis.take().lower()

            #     Logic -->

            if query == None or "exit" in query:
                speak("Exiting")
                exit()

            # Execute only if user said Jarvis -->


            if "search" in query:
                jarvis.search(query)

            elif "chatbot" in query:
                jarvis.chatbot()

            elif "wikipedia" in query:
                jarvis.wikipedia_func(query)

            elif "weather" in query:
                jarvis.weather()

                elif "temprature" in query:
                    jarvis.temprature()

                elif "hacking" in query:
                    command = 'matrix.bat'
                    subprocess.run(["start", "/wait", "cmd", "/K", command, "arg /?\^"], shell=True)

                elif "open" in query:
                    open_query = query[5:]

                    if "code" in open_query:
                        subprocess.Popen(
                                    "C:\\Users\\Lakshya Bhawsar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                        exit()
                    elif "chrome" in open_query:
                        subprocess.Popen(
                                    "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe")
                        exit()

                    elif "gta" or "gta 5" in open_query:
                        subprocess.Popen(
                                    "C:\\DISK E\\Games\\Grand Theft Auto V OPEN\\GameLauncher.exe")
                        exit()

                    elif "rocket" or "league" in open_query:
                        subprocess.Popen(
                                    "C:\\DISK E\\Games\\rocketleague\\Binaries\\Win64\\RocketLeague.exe")
                        exit()

                    elif "youtube" or "you" or "tube" in open_query:
                        speak("Opening Youtube")
                        url = 'https://youtube.com'
                        webbrowser.open(url)
                        exit()

                    else:
                        pass

                elif "music" in query:
                    url = 'https://www.youtube.com/watch?v=iTTqlnKyRME&list=RDMM&start_radio=1'
                    webbrowser.open(url)
                    exit()

                elif "joke" in query:
                    My_joke = pyjokes.get_joke(language="en", category="all")
                    print(My_joke)
                    speak(My_joke)

                elif "insult" or "roast" in query:
                    jarvis.insult()

                elif "dice" in query:
                    jarvis.rolldice()

                elif "flip" or "coin" in query:
                    jarvis.flipcoin()

                elif "rate" in query:
                    rate = random.randint(0, 10)
                    speak("I will rate this as {rate} out of ten")

                elif "hi" or "hello" in query:
                    greet = ["hi ", "hello ", "What's Up "]
                    rgreet = random.choice(greet)
                    speak(rgreet)

                elif "say" in query:
                    if query == None:
                        speak("How can i say nothing , Fool ")
                    else:
                        query2 = query[3:]
                        speak(query2)
                elif "how" in query:
                    if "cool" in query:
                        rhot = random.randint(0, 100)
                        speak(f"You are {rhot} percent cool")
                    elif "horny" in query:
                        rhot = random.randint(0, 100)
                        speak(f"You are {rhot} percent horny")
                    elif "hot" in query:
                        rhot = random.randint(0, 100)
                        speak(f"You are {rhot} percent hot")
                    elif "gay" in query:
                        rhot = random.randint(0, 100)
                        speak(f"You are {rhot} percent gay")

                elif "calculate" and "iq" in query:
                    rhot = random.randint(0, 100)
                    speak(f"Your iq percentage is {rhot}")

                elif "exit" or "quit" in query:
                    speak("Power , Off")
                    exit()

                elif query == None or query == None:
                    speak("Power , Off")
                    exit()

                else:
                    speak("I don't have this feature yet")
            else:
                print('jarvis not said')
                pass
    except Exception as e:
        print(e)



