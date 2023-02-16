from PyDictionary import PyDictionary
import json
import cv2
import pytesseract
import time
import pickle
import numpy as np
from PIL import ImageGrab
import pyautogui

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
dictionary = PyDictionary()
words = []
#sentence = input("Sentence:")

def captureScreen(bbox=(0,0,1919,1079)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr

def img2Word():
    time.sleep(5)
    timer = cv2.getTickCount()
    img = captureScreen()
    img = img[184:1058, 1006:1633]
    word = pytesseract.image_to_string(img)
    return word
    # hImg, wImg,_ = img.shape
    # boxes = pytesseract.image_to_boxes(img)
    # for b in boxes.splitlines():
    #     b = b.split(' ')
    #     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #     cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    #     cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
    # cv2.imshow("cropped", img)
    # cv2.waitKey(0)
def clearWords(words):
    cleanWords=[]
    symbols = [chr(y) for y in range(32,65)]
    symbols.extend([chr(x) for x in range(91,97)])
    symbols.extend(['"',"'","{","}","|","~",'\t','\n','©'])
    for word in words:
        for y in symbols:
            word = word.replace(y,'')
        if word not in cleanWords and word != '':
            cleanWords.append(word)
    return cleanWords

def sentence2words():
    # with open(r'data\wordsdata\sentence.txt','r') as files:
    #     line=files.readline()
    words = img2Word().split()
    #print(words)
    cleanWords = clearWords(words)
    #print(cleanWords)
    try:
        with open(r'.\data\wordsdata\words.pkl','rb') as files:
            loadWords = pickle.load(files)
        for i in cleanWords:
            if i not in loadWords:
                loadWords.append(i)
        print(loadWords)
        with open(r'.\data\wordsdata\words.pkl','wb') as files:
            pickle.dump(loadWords,files)
    except FileNotFoundError:
        with open(r'.\data\wordsdata\words.pkl','wb') as files:
            pickle.dump(cleanWords,files)
    except Exception as e: print(e)

def get_grammar(line):
    words = line.split()
    grammar_format = {}
    get_meaning = {}
    print(words)
    for word in words:
        print(word)
        #word = word.replace(rmove,"") for rmove in ['.','/','?',',','(',]
        get_meaning = dictionary.meaning(word)
        print(get_meaning)
        grammar_format[word]=get_meaning

    print("\n")    
    print(grammar_format)
    

if __name__ == '__main__':
    for i in range(2475,100000):
        print(i)
        buttonlocation= None 
        while buttonlocation is None:
            buttonlocation = pyautogui.locateOnScreen(r'.\data\wordsdata\image\button.png')
        #print(buttonlocation)
        x,y,x_,y_ = buttonlocation
        time.sleep(5)
        pyautogui.click(x+x_/2, y+y_/2)
        pyautogui.move(0,100)
        sentence2words()

        
        
        #sentence2words()