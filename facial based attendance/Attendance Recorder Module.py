import cv2
import numpy as np
from PIL import Image
import os, pandas as pd
from tkinter import messagebox
from datetime import datetime

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
            PIL_img = Image.open(image_path).convert('L') # grayscaling the image
            img_numpy = np.array(PIL_img,'uint8')
            id = int(os.path.split(image_path)[-1].split(".")[1])
            faces = self.detector.detectMultiScale(img_numpy)
            for (x,y,w,h) in faces:
                face_samples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return face_samples, ids

    def train_recognizer(self):
        """Train the recognizer model using the available face data."""
        faces, ids = self.get_images_and_labels