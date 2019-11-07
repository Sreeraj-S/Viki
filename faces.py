import numpy
import cv2
import pickle
import pyttsx3
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
face_dic =  ["hi","hey","sup","how are you","how may i help you"]
face_cascade = cv2.CascadeClassifier('F:\\sreeraj\\viki\\cascade\\data\\haarcascade_frontalface_alt2.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
wish_me=[]
labels={}
with open("labels.pickle",'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap=cv2.VideoCapture(0)

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
            print(id_)
            #print(labels[id_])
            font = cv2.FONT_HERSHEY_COMPLEX
            name=labels[id_]
            colour = (255,255,255)
            stroke = 2
            cv2.putText(frame,name,(x,y),font,1,colour,stroke,cv2.LINE_AA)
            if labels[id_] not in wish_me:
                a = random.choices(face_dic)
                speak(f"{a}{labels[id_]}")
                wish_me=[]
                wish_me.append(labels[id_])

        img_items = "my_image.png"
        cv2.imwrite(img_items, roi_gray)

        color = (255,0,0)
        stroke=2
        end_x=x+w
        end_y=y+h
        cv2.rectangle(frame,(x,y),(end_x,end_y),color,stroke)

    cv2.imshow("frame",frame)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()