import os
import cv2
from tkinter import *
from tkinter import messagebox
import pandas as pd

class User:
    """User class to store registered user details."""
    def __init__(self, id, name):
        """Initializes User with given id and name.

        Args:
        id (str): User's unique id.
        name (str): User's name.
        """
        self.id = id
        self.name = name

def register_face(user):
    """Register face of user by capturing imaes and store the corresponding details.
    Args:
    user (User): A User object containing user details.
    """
    messagebox.showinfo('Instructions', 'Please make sure the camera captures your face.')
    cap = cv2.VideoCapture(0)
    count = 0
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        cv2.imwrite(f"dataset/User.{user.id}.{count}.jpg", gray)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q') or count==100:
            break

    chunksize = 10 ** 5
    if not os.path.isfile('registered_users.csv'):
        df = pd.DataFrame(columns=['ID', 'Name'])
        df.to_csv('registered_users.csv', index=False)
    df = pd.DataFrame([{'ID':user.id, 'Name':user.name}], columns=['ID', 'Name'])
    for chunk in pd.read_csv('registered_users.csv', chunksize=chunksize):
        df = pd.concat([chunk, df])
    df.to_csv('registered_users.csv', index=False)
    cap.release()
    cv2.destroyAllWindows()

def verify_data(user):
    """Verify the correctness of stored data against given user's details.

    Args:
    user (User): A User object containing user details to be verified.
    """
    df = pd.read_csv('registered_users.csv')
    if df.loc[df['ID'] == int(user.id), 'Name'].iloc[0] == user.name:
        messagebox.showinfo('Success', 'Registration and verification successful.')
    else:
        messagebox.showinfo('Failure', 'Verification Failed! Please try again.')

def start_process():
    """ Triggered upon button press on the GUI, instantiates User and starts face registration."""
    id = id_entry.get()
    name = name_entry.get()
    user = User(id, name)
    register_face(user)
    verify_data(user)

    id_entry.delete(0, END)
    name_entry.delete(0, END)

# Create a window using Tkinter
window = Tk()
window.title("Face Registration")

Label(window, text="User ID").pack()
id_entry = Entry(window)
id_entry.pack()

Label(window, text="Name").pack()
name_entry = Entry(window)
name_entry.pack()

Button(window, text="Start Face Registration", command=start_process).pack()

window.mainloop()
