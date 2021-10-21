from sys import modules
import pyttsx3
import speech_recognition as sr
import datetime
from modules.wikipedia.wikipedia_module import wiki
from modules.apps import train as software_train,software
from modules.jokes.joke import jokes
from modules.music.main import searchVideoID

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

wish_me=[]

def speak(audio):
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

    speak("I am Viki. Please tell me how may I help you") 

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 450
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        ##root.usercommand(query)
        print(f"User said: {query}")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query 

def WakeUp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Wake me..")
        r.pause_threshold = 0.5
        r.energy_threshold = 450
        audio = r.listen(source)

    try:    
        print("Recognizing...")  
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
          
        return "None"
    return query

if __name__ == "__main__":
    
    Wish=''
    wishMe()
    while True:
        if not "viki" == Wish:
            Wish = WakeUp().lower()
        if 'wiki' in Wish or 'viki' == Wish:
            speak("hey there")
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                speak(wiki(query))
    
