import cv2
import numpy as np

import os, pandas as pd
from datetime import datetime
from tkinter import *
from PIL import Image

# Path for face image database
path = 'dataset'

class FaceRecognition:
    """Handles facial recognition operations"""

    def __init__(self):
        """Initializes FaceRecognition with the settings."""
        self.detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

    def get_images_and_labels(self):
        """Fetch image and label data for training recognizer."""
        image_paths = [os.path.join(path,f) for f in os.listdir(path)]     
        face_samples = []
        ids = []
        for image_path in image_paths:
            PIL_img = Image.open(image_path).convert('L') # grayscale conversion
            img_numpy = np.array(PIL_img,'uint8')
            id = int(os.path.split(image_path)[-1].split(".")[1])
            faces = self.detector.detectMultiScale(img_numpy)
            for (x,y,w,h) in faces:
                face_samples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return face_samples, ids

    def train_recognizer(self):
        """Train the recognizer model using available face data."""
        faces, ids = self.get_images_and_labels()
        self.recognizer.train(faces, np.array(ids))

    def perform_recognition(self):
        """Perform live facial recognition, logs attendance and return details for recognized faces."""
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        while True:
            _, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.detector.detectMultiScale(gray)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                id, confidence = self.recognizer.predict(gray[y:y+h,x:x+w])

                # if confidence is less than 100 -> "0" perfect match 
                if (confidence < 100):
                    df_registered = pd.read_csv('registered_users.csv')
                    user_name = df_registered.loc[df_registered['ID'] == id, 'Name'].iloc[0]
                    confidence = "  {0}%".format(round(100 - confidence))

                    df_attendance = pd.read_csv('attendance.csv')
                    new_index = len(df_attendance)
                    df_attendance.loc[new_index] = {'ID': id, 'Name': user_name, 'Date': datetime.today().strftime('%Y-%m-%d'), 'Time In': datetime.now().strftime('%H:%M:%S')}
                    df_attendance.to_csv('attendance.csv', index=False)
                else:
                    id = "unknown"

                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 2)

            cv2.imshow('camera', img) 
            # Press 'ESC' for exiting video
            k = cv2.waitKey(10) & 0xff 
            if k == 27: 
                break

        cam.release()
        cv2.destroyAllWindows()

def start_process():
    """Starts the face recognition process upon GUI button press."""
    recog = FaceRecognition()
    recog.train_recognizer()
    recog.perform_recognition()

# Create a window in Tkinter
window = Tk()
window.title("Face Recognition")

Button(window, text="Start Face Recognition", command=start_process).pack()

window.mainloop()
