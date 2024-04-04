import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pynput#pip install pynput
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
from gtts import gTTS#pip install gtts
import numpy
from PIL import Image 
import requests
import random
import threading
import serial
#import Viki_gui

listuser={}

#root = Viki_gui.Gui()
# init_bg = ['F:\\sreeraj\\viki\\initpic\\Init0.png','F:\\sreeraj\\viki\\initpic\\Init.0.png','F:\\sreeraj\\viki\\initpic\\Init..0.png','F:\\sreeraj\\viki\\initpic\\Init...0.png','F:\\sreeraj\\viki\\initpic\\Init.1.png','F:\\sreeraj\\viki\\initpic\\Init..1.png']


try:
    arduinodata = serial.Serial('com3',9600)
    n = bytes("n", 'utf-8')
    l = bytes("l", 'utf-8')
    f = bytes("f", 'utf-8')
    a = bytes("a", 'utf-8')
except:
    pass
intents={"intents":[
    {
    "tag":"greetings",
    "patterns":["hi","is anyone there","hello"],
    "responese":["Hello","Hi there, How can i help you"],
    "context_set":""
    },
    {
    "tag":"goodbye",
    "patterns":["tata","goodbye","see you later"],
    "responese":["Sad to See you go","Talk to you later","Goodbye","Bye"],
    "context_set":""
    },
    {
    #"tag":"marry"
    "patterns":["will you marry me"],
    "responese":["srry it is biologicaly not possible","srry it is physically not possible","srry it is chemically not possible"]
    },
    {
    "patterns":["i love you","i like you"],
    "responese":["i like you too","me too But lets be Friends"]
    },
    {
    "patterns":["who are u"],
    "responese":["I am Viki,An AI"]
    },
    {
    "patterns":["how are you","you good"],
    "responese":["great,U need help","fine","thats so nice of you,I am fine",]
    },
    {
    "patterns":["thank you"],
    "responese":["YOur welcome,I am always there for you"]
    }

]}

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
    "fardheen":"fardheenbkurdheen@gmail.com",
    "shivnandan":"shivnandnanskakkalil@gmail.com"}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

wish_me=[]
face_dic =  ["hi","hey","sup","how are you","how may i help you"]

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
    #root.compcommand("I am Viki. Please tell me how may I help you")
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
        r.pause_threshold = 1
        audio = r.listen(source)

    try:    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
          
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ai.assistant101@gmail.com', 'VIKI1209')
    server.sendmail('ai.assistant101@gmail.com', to, content)
    server.close()
def lights_on():
    try:
        arduinodata.write(l)
    except:
        speak("Bluetooth Not coNNected")  
def lights_off():
    arduinodata.write(f)
def fan_on():
    arduinodata.write(a)
def fan_off():
    arduinodata.write(n)

if __name__ == "__main__":
    """speak("initializing")
    time.sleep(12)
    ##root.initreset()
    time.sleep(0.5)
    speak("loading")
    time.sleep(10)
    ##root.loadreset()
    time.sleep(0.5)
    speak("runing full Test")
    time.sleep(5)
    speak("please Wait for a moment")
    time.sleep(4)
    time.sleep(3.6)
    speak("WE miss you MAHATHMA GANDHI")
    time.sleep(10)
    ##root.mahareset()
    time.sleep(1)"""





    Wish=''
    wishMe()
    #thread.start()
    while True:

        if not "viki" == Wish:
            Wish =WakeUp().lower()
        #Wish=input("wake me")
        
        for i in range(len(intents["intents"])):
            for j in range(len(intents["intents"][i]["patterns"])):
                lis=intents["intents"][i]["responese"]
                if  intents["intents"][i]["patterns"][j] in Wish:
                    speak(random.choice(lis))
    
        if 'wiki' in Wish or 'viki' == Wish:
            if not 'viki' == Wish:
                speak("hey there")
            for Repeat in range(3):
                query = takeCommand().lower()
                #query = input("type:")
                if 'wikipedia' in query:
                    ##root.compcommand('Searching Wikipedia...')
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    ##root.compcommand("According to Wikipedia")
                    speak("According to Wikipedia")
                    ##root.compcommand(results)
                    speak(results)
                    break
                elif "who is" in query:
                    try:
                        query = query.replace("who is", "")
                        results = wikipedia.summary(query, sentences=2)
                        ##root.compcommand(results)
                        speak(results)
                    except:
                        speak("i don't Know that Person,should I search Google")
                        ##root.compcommand("i don't Know that Person,should I search Google")
                        search=query
                        query=takeCommand().lower()
                        if "yes" in query:
                            webbrowser.open(f"https://www.google.com/search?q={search}")
                        else:
                            speak("Ok")
                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                    break
                elif 'create list' in query:
                    speak("what is List Name?")
                    lis=takeCommand().lower()
                    speak("What Should I add in the list")
                    listtake=takeCommand().lower()
                    spllitlis=listtake.split()
                    listuser[lis]=spllitlis
                elif ("show" in query and ("items" in query or 'item' in query)) or ("show" in query and 'list' in query):
                    if "show" in query and 'list' in query:
                        showlis=query.replace("show",'')
                        showlis=showlis.replace("list",'')
                        print(listuser[showlis])
                        for lisloop in listuser[showlis]:
                            speak(lisloop)
                    else:
                        speak("WHich liSt")
                        showlis=takeCommand().lower()
                        print(listuser[showlis])
                        for lisloop in listuser[showlis]:
                            speak(lisloop)
                    

                elif 'open google' in query:
                    webbrowser.open("google.com")
                    break
                elif 'search google' in query:
                    search=query.replace("search google",'')
                    webbrowser.open(f"https://www.google.com/search?q={search}")
                elif 'search youtube' in query:
                    search=query.replace("search youtube",'')
                    webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")
                    break   

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
                        break
                    else:
                        choose=query.replace("play ","")
                        webbrowser.open("https://www.youtube.com/results?search_query="+choose)
                        time.sleep(10)
                        mouse.position = (405, 325)
                        mouse.click(Button.left,1)
                        time.sleep(5)
                        #mouse.position = (337, 387)
                        #mouse.click(Button.left,1)
                        break
                elif 'joke' in query:
                    res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"}
                )       
                    if res.status_code == requests.codes.ok:
                        joke = str(res.json()['joke'])
                        speak(joke)
                        print(joke)
                    else:
                        speak('oops!I ran out of jokes')
                    break

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif 'open code' in query:
                    codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                elif "open libaries" in query:
                    codePath = "C:\\Windows\\explorer.exe"
                    os.startfile(codePath)
                elif 'turn on light' in query:
                    lights_on()
                elif "turn off light" in query:
                    lights_off()
                elif "turn on fan" in query:
                    fan_on()
                elif "turn off fan" in query:
                    fan_off()
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
                else:
                    if not query == "none":
                        choose = query
                        speak("should I search in google Or Play the music")
                        query=takeCommand().lower()
                        if "play the music" in query or "play the song" in query or "the song" in query:
                            webbrowser.open("https://www.youtube.com/results?search_query="+choose)
                            time.sleep(10)
                            mouse.position = (405, 325)
                            mouse.click(Button.left,1)
                            time.sleep(5)
                        elif "search google" in query or "search" in query:
                            webbrowser.open(f"https://www.google.com/search?q={choose}")
                Wish=''
        elif 'good morning' in Wish or 'good afternoon' in Wish or 'good afternoon' in Wish:
            hour = int(datetime.datetime.now().hour)
            if 'good morning' in Wish:
                Wish = 'good morning'
            elif 'good afternoon' in Wish:
                Wish = 'good afternoon'
            if hour>=0 and hour<12:
                if 'good morning' in Wish:
                    speak("Good Morning!")
                else:
                    speak('it is Morning only')

            elif hour>=12 and hour<18:
                
                if 'good afternoon' in Wish:
                    speak("Good Afternoon!")
                else:
                    speak('it is Afternoon time')

            else:
                speak("Good Evening!")
                if 'good evening' in Wish:
                    speak("Good Evening!")
                else:
                    speak(f'tHE SUN IS down,still u say{Wish}')
        elif "yes" in Wish or "yeah" in Wish:
            speak("How may I help YOu?")
            Wish="viki"
        elif "i need help" in Wish or "help me" in Wish:
            speak('ok,tell me')
            Wish = 'viki'


