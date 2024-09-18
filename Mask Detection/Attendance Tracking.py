import cv2
#import face_recognition
from datetime import datetime
import csv
from cryptography.fernet import Fernet

class AttendanceTracker:
    """
    Class to track attendance using facial recognition and store it into a CSV file.
    """
    def __init__(self, images_dir, key):
        """
        Initialize Attendance tracker with directory of images and encryption key
        Parameters:
        images_dir : str : path to directory with facial images
        key : byte string : secret key for encrypting and decrypting CSV file
        """
        self.encodings = []
        self.names = []
        self.images_dir = images_dir
        self.fernet = Fernet