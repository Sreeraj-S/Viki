
import numpy
import cv2


face_cascade = cv2.CascadeClassifier('F:\sreeraj\viki\cascades\data\haarcascade_frontalface_alt2.xml')



camera_port = 0
#camera = cv2.VideoCapture(camera_port)
camera = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)
# Check if the webcam is opened correctly
if not camera.isOpened():
    raise IOError("Cannot open webcam")
for i in range (5):
    return_value, image = camera.read()
    print("We take a picture of you, check the folder")

    cv2.imwrite(f"{i}.png", image)

camera.release() # Error is here
cv2.destroyAllWindows()
