import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pynput
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

intents={"intents":[
    {"tag":"greetings",
    "patterns":["hi","how are you","is anyone there","hello"],
    "responese":["Hello","Great","Hi there, How can i help you"],
    "context_set":""
    },
    {"tag":"goodbye",
    "patterns":["tata","goodbye","see you later"],
    "responese":["Sad to See you go","Take to later","Goodbye","Bye"],
    "context_set":""}]}

keyboard = KeyboardController()
mouse = MouseController()
domain_dict={"gmail":"@gmail.com",
    "hotmail":"@hotmail.com",
    "yahoo":"@yahoo.com",
    }
email={
    "sreeraj":"sathishranji1@gmail.com",
    "nikhil":"nikhilkartha724@gmail.com",
    "rishi":"hrishikeshms1020@gmail.com",
    "akshith":"akshithrajeev77@gmail.com",
    "fardheen":"fardheenbkurdheen@gmail.com"}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


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
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def WakeUp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:    
        print('recognising')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
          
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ai.assistant101@gmail.com', 'VIKI1209')
    server.sendmail('ai.assistant101@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        Wish =takeCommand().lower()
        if 'wiki' in Wish:
            speak("yes sir")
            for Repeat in range(3):
                query = takeCommand().lower()
            
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")   


                elif 'play' in query or 'music' in query:
                    if 'play music' in query:
                        speak("which song")
                        choose=takeCommand().lower()
                        webbrowser.open("https://www.youtube.com/results?search_query="+choose)
                        time.sleep(10)
                        mouse.position = (405, 325)
                        mouse.click(Button.left,1)
                        time.sleep(5)
                        #mouse.position = (337, 387)
                        #mouse.click(Button.left,1)
                    else:
                        choose=query.replace("play ","")
                        webbrowser.open("https://www.youtube.com/results?search_query="+choose)
                        time.sleep(10)
                        mouse.position = (405, 325)
                        mouse.click(Button.left,1)
                        time.sleep(5)
                        #mouse.position = (337, 387)
                        #mouse.click(Button.left,1)
                elif 'joke' in query:
                    res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"}
                )       

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif 'open code' in query:
                    codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif 'send email' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        speak("To whom Should I send?")
                        to=takeCommand().lower()
                        if "@gmail.com" in to:   
                            sendEmail(to, content)
                            speak("Email has been sent!")
                            break
                        else:
                            if to in email.keys():
                                repeat=0
                                while repeat == 0:
                                    to=email[to]
                                    if "none" in to:
                                        pass
                                    else:
                                        repeat+=1
                                sendEmail(to, content)
                                speak("Email has been sent!")
                                break
                            else:
                                speak("Sorry sir.There is no One in this name stored")
                                speak("please tell me the email id")
                                to=takeCommand().lower()
                                if "cancel" == to:
                                    break
                                to_withnospace_list=to.split()
                                to_withnospace=""
                                for to_variable in to_withnospace_list:
                                    to_withnospace += to_variable
                                speak("please say which Domain is it")
                                domain=takeCommand().lower()
                                to_withnospace += domain_dict[domain]
                                sendEmail(to_withnospace, content)
                                speak("Email has been sent!")
                                break
                    except Exception as e:
                        print(e)
                        speak("Sorry sir  I am not able to send this email") 
                elif 'shutdown' in query or "quit" in query:
                    speak('are you sure')
                    content=takeCommand().lower()
                    if 'yes'==content or 'sure' == content:
                        speak('bye')
                        quit()
                    elif 'no'==content or 'nah'==content:
                        pass
