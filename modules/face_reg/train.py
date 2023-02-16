import face_recognition
import os, sys
import cv2
import numpy as np
import math


# Helper
def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'


class FaceRecognition:
    img_file_loc = r'.\data\faceregdata\images\sreeraj'
    img_loc = r'.\data\faceregdata\images'
    face_locations = []
    face_encodings = []
    face_names = []
    no_face = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True
    confidence = ''
    img_name = 0
    file_no =[]

    def __init__(self):
        #self.run_recognition()
        self.encode_faces()
        

    def encode_faces(self):
        for image in os.listdir(self.img_file_loc):
            face_image = face_recognition.load_image_file(os.path.join(self.img_file_loc,image))
            try:
                face_encoding = face_recognition.face_encodings(face_image)[0]
                self.known_face_encodings.append(face_encoding)
                self.known_face_names.append(image)
            except:
                self.no_face.append(image)
        for fiPa in self.no_face:
            os.remove(os.path.join(self.img_file_loc,fiPa))
        for dirpath, dirnames, files in os.walk(self.img_loc, topdown=False):
                        print(f'Found directory: {dirpath}')
                        self.file_no = [int(file_name.replace('.jpg','')) for file_name in files]
                        print(self.file_no)
                        self.file_no.sort()
       
    def run_recognition(self):
        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            sys.exit('Video source not found...')

        while True:
            ret, frame = video_capture.read()

            # Only process every other frame of video to save time
            if self.process_current_frame:
                # Resize frame of video to 1/4 size for faster face recognition processing
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                rgb_small_frame = small_frame[:, :, ::-1]

                # Find all the faces and face encodings in the current frame of video
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"
                    confidence = '???'

                    # Calculate the shortest distance to face
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)

                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        self.confidence = face_confidence(face_distances[best_match_index])

                    self.face_names.append(f'{name} ({self.confidence})')
                #print(self.face_names)

            self.process_current_frame = not self.process_current_frame
            if self.confidence != '' and self.face_names!=[]:
                print(self.confidence)
                if float(self.confidence.replace('%','')) > 97 and self.img_name != 100:
                    print("here")
                    if self.img_name in self.file_no:
                        self.img_name+=1
                        print(self.img_name)
                    else:
                        cv2.imwrite(os.path.join(self.img_file_loc, f'{self.img_name}.jpg'),frame)
                        self.img_name+=1

            # Display the results
            # for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            #     top *= 4
            #     right *= 4
            #     bottom *= 4
            #     left *= 4

            #     # Create the frame with the name
            #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            #     cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Face Recognition', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    fr = FaceRecognition()
    fr.run_recognition()