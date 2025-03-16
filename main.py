import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import calendar
import wolframalpha
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import pepper
import nltk
from nltk.corpus import wordnet
import re
import string
import pywhatkit
from bs4 import BeautifulSoup
import requests
import keyboard
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import subprocess
import wave


p = re.compile("["+ re.escape(string.punctuation)+"]")
syns = wordnet.synsets("turn off")


client = wolframalpha.Client('RK43HA-E33E3XRE3J')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" 
    }

# scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# creds = ServiceAccountCredentials.from_json_keyfile_name('Client_secret.json',scope)

# client = gspread.authorize(creds)
# sheet = client.open('home_automation_database').sheet1

# setup = pd.read_csv(r"C:\Users\mukun\OneDrive\Desktop\SARA - final\setup.txt", sep='=', index_col=0, squeeze=True, header=None)
# client_id = setup['client_id']
# client_secret = setup['client_secret']
# device_name = setup['device_name']
# redirect_uri = setup['redirect_uri']
# scope = setup['scope']
# username = setup['username']



# reminder_path = "C:\\Users\\mukun\\OneDrive\\Desktop\\SARA - final\\reminder system2.py"
# p1 = multiprocessing.Process(target=run_code,args=['reminder system2.py'])





# auth_manager = SpotifyOAuth(
#     client_id=client_id,
#     client_secret=client_secret,
#     redirect_uri=redirect_uri,
#     scope=scope,
#     username=username)
# spotify = spotipy.Spotify(auth_manager=auth_manager)

# devices = spotify.devices()
# deviceID= None


# for d in devices['devices']:
#     d['name'] = d['name'].replace('`', '\'')
#     if d['name'] == device_name:
#         deviceID = d['id']
#         break
#    
# def get_track_uri(spotify: spotify, query: str) -> str:
#     global track_uri
#     results = spotify.search(q=query, limit=1, type='track')
#     if not results['tracks']['items']:
#         raise InvalidSearchError(f'Sorry no song named{query}')
#     track_uri = results['tracks']['items'][0]['uri']
#     query = query.replace('', '+')
#     return track_uri
#     print(track_uri)

# def play_track(spotify=None, device_id=None, uri=None):
#     spotify.start_playback(device_id=device_id, uris=[uri])


# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo() 
#     server.starttls()
#     server.login('mukundmv08@gmail.com', '')
#     server.sendmail('mukundmv08@gmail.com', to, content)
#     server.close()

def run_code(file_name):
    subprocess.run('python3', f"filename")   

def speak(audio):   
    rate = engine.getProperty("rate")
    engine.setProperty("rate",170)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")       

def takeCommand():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.2)
        print(f"Set minimum energy threshold to {r.energy_threshold}")
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    #os.startfile(reminder_path)
    while True:
        query = takeCommand().lower()
        if 'asian gpt' in query: 
            if query == "":
                query = takeCommand().lower()
            # print("active...")
            # query = takeCommand().lower()
        if 'give me a list of universities to apply to' in query:
            speak("ill give you two option either community college near your city or far from it")
        if "what is 2 + 2" in query:
            speak("you stuppid u cant even do simple maths")
        if "my friends are coming over can you give me party ideas" in query:
            speak("why are you lying you have no friens")