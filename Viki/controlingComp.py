import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time
import pyautogui
 
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('1.png')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
##############################################
##### Webcam and Screen Capture Example ######
##############################################
#cap = cv2.VideoCapture(0)
#cap.set(3,640)
#cap.set(4,480)
def captureScreen(bbox=(0,0,1365,767)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr
while True:
    timer = cv2.getTickCount()
    #_,img = cap.read()
    img = captureScreen()
    #DETECTING CHARACTERES
    hImg, wImg,_ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        #cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
        #cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
    #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    #cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20,230,20), 2);
    word = pytesseract.image_to_string(img)
    print(word)
    #cv2.imwrite("Result.jpg",img)
    cv2.waitKey(1)
    print('-----------------------------------------------')