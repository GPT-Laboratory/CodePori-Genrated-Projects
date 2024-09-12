
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import threading
from face_register import *
from face_recognizer import *
from manual_override import *

REGISTERED_USERS_FILE = 'registered_users.csv'
ATTENDANCE_FILE = 'attendance.csv'

class AttendanceSystemUI:

    def __init__(self):
        """ Initializes the tkinter GUI and camera for feed """
        self.window = tk.Tk()
        self.window.title("Attendance System")
        self.window.geometry('900x600')

        self.vid = cv2.VideoCapture(0) 
        self.canvas = tk.Canvas(self.window, width=850, height=400)
        self.canvas.grid(row=1, column=0, columnspan=4)

        self.delay = 15
        self.update()

        self.create_widgets()

    def create_widgets(self):
        """ Creates required tkinter widgets """
        Button(self.window, text="Start Camera", command=self.start_camera).grid(row=0, column=0)
        Button(self.window, text="Add Person", command=self.add_person).grid(row=0, column=1)
        Button(self.window, text="Manual Attendance", command=self.manual_attendance).grid(row=0, column=2)
        Button(self.window, text="EXIT", command=self.close).grid(row=0, column=3)

        Label(self.window, text="Details of the last recognized person, if any :").grid(row=2, column=0)
        self.last_user_lbl = Label(self.window, text="-", width=50)
        self.last_user_lbl.grid(row=2, column=1)

        Label(self.window, text="Full Attendance Data : ").grid(row=3, column=0)
        self.attendance_box = Listbox(self.window, width=50)
        self.attendance_box.grid(row=3, column=1)

        self.view_logs()

    def start_camera(self):
        """ Triggered upon button press on the GUI, starts new thread for FaceRecognition """
        threading.Thread(target=self.start_recognition).start()

    def add_person(self):
        """ Triggered upon button press on the GUI, starts new thread for FaceRegistration """
        threading.Thread(target=self.start_registration).start()

    def manual_attendance(self):
        """ Triggered upon button press on the GUI, starts new thread for ManualOverride """
        threading.Thread(target=self.start_manual_override).start()

    def close(self):
        """ Quits application """
        self.vid.release()
        self.window.quit()

    def update(self):
        """ Updates video frames in GUI """
        ret, img = self.vid.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update)

    def show_status(self, username):
        self.last_user_lbl.config(text=f'Usernam')
    
    def view_logs(self):
        self.attendance_register = pd.read_csv(ATTENDANCE_FILE)
        self.attendance_box.delete(0, END)
        for i, row in self.attendance_register.iterrows():
            self.attendance_box.insert(END,  f'User: {row.ID} - Date: {row.Date} - Time-In: {row["Time In"]} - Time-Out: {row["Time Out"]}')


    def start_recognition(self):
        recog = FaceRecognition()
        recog.train_recognizer()
        recognized_name = recog.perform_recognition()
        self.show_status(recognized_name)
        self.view_logs()

    def start_registration(self):
        register_face()

    def start_manual_override(self):
        # manual_override()
        self.view_logs()

if __name__ == "__main__":
    AttendanceSystemUI().window.mainloop()
