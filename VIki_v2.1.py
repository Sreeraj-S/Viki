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
from gtts import gTTS
import numpy

from PIL import Image, ImageTk 
import requests
import random
import threading
import serial


init_bg = ['F:\\sreeraj\\viki\\initpic\\Init0.png','F:\\sreeraj\\viki\\initpic\\Init.0.png','F:\\sreeraj\\viki\\initpic\\Init..0.png','F:\\sreeraj\\viki\\initpic\\Init...0.png','F:\\sreeraj\\viki\\initpic\\Init.1.png','F:\\sreeraj\\viki\\initpic\\Init..1.png']


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
    "patterns":["hi","how are you","is anyone there","hello"],
    "responese":["Hello","Great","Hi there, How can i help you"],
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
    "responese":["srry it is biologicaly not possible"]
    },
    {
    "patterns":["i love you","i like you"],
    "responese":["i like you too","me too But lets be Friends"]
    },
    {
    "patterns":[""],
    "responese":[""]
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
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

wish_me=[]
face_dic =  ["hi","hey","sup","how are you","how may i help you"]

"""def tkinterinit(commandtk):
    
    root=Tk()
    while True:       
        if commandtk == "init":
            load_init_bg=ImageTk.PhotoImage( Image.open(init_bg[0]))
            init_bg_exe= Label(root,image=load_init_bg)
            init_bg_exe.pack()
            time.sleep(1)
            for init_bg_loop in range(len(init_bg)):
                init_bg_exe.pack_forget()
                load_init_bg=ImageTk.PhotoImage( Image.open(init_bg[init_bg_loop]))
                init_bg_exe= Label(root,image=load_init_bg)
                init_bg_exe.pack()
                time.sleep(2)
            commandtk=''
    mainloop()"""

        

"""def face_recog():
    
    
    face_cascade = cv2.CascadeClassifier('F:\\sreeraj\\viki\\cascade\\data\\haarcascade_frontalface_alt2.xml')
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainner.yml")
    
    labels={}
    with open("labels.pickle",'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}
    while True:
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
        
        for (x,y,w,h) in faces:
                #print(x,y,w,h)
            roi_gray = gray [y:y+h, x:x+w]
            roi_colour = frame[y:y+h, x:x+w]

            id_,conf = recognizer.predict(roi_gray)
            if conf>=45 and conf<=85:

                font = cv2.FONT_HERSHEY_COMPLEX
                name=labels[id_]
                recog_name=labels[id_]
                colour = (255,255,255)
                stroke = 2
                cv2.putText(frame,name,(x,y),font,1,colour,stroke,cv2.LINE_AA)
                
               

                img_items = "my_image.png"
                cv2.imwrite(img_items, roi_gray)

                color = (255,0,0)
                stroke=2
                end_x=x+w
                end_y=y+h
                cv2.rectangle(frame,(x,y),(end_x,end_y),color,stroke)

        #cv2.imshow("frame",frame)
        if cv2.waitKey(20) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()"""


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
    arduinodata.write(l)    
def lights_off():
    arduinodata.write(f)
def fan_on():
    arduinodata.write(a)
def fan_off():
    arduinodata.write(n)

if __name__ == "__main__":
    
    speak("initializing")
    time.sleep(12)
    speak("loading")
    time.sleep(10)
    speak("runing full Test")
    time.sleep(5)
    speak("please Wait for a moment")
    time.sleep(4)





    wishMe()
    #thread.start()
    while True:      

        Wish =WakeUp().lower()
        #Wish=input("wake me")
        
        for i in range(len(intents["intents"])):
            for j in range(len(intents["intents"][i]["patterns"])):
                lis=intents["intents"][i]["responese"]
                if  intents["intents"][i]["patterns"][j] in Wish:
                    speak(random.choice(lis))
    
        if 'wiki' in Wish:
            speak("hey there")
            for Repeat in range(3):
                query = takeCommand().lower()
                #query = input("type:")
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                    break
                elif "who is" in query:
                    try:
                        query = query.replace("who is", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak(results)
                    except:
                        speak("i don't Know that Person,should I search Google")
                        search=query
                        query=takeCommand().lower()
                        if "yes" in query:
                            webbrowser.open(f"https://www.google.com/search?q={search}")
                        else:
                            speak("Ok")
                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                    break

                elif 'open google' in query:
                    webbrowser.open("google.com")
                    break

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



