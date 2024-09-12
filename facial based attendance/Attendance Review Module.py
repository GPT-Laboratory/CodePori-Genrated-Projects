import pandas as pd
from tkinter import *
from tkinter import messagebox

REGISTERED_USERS_FILE = 'registered_users.csv'
ATTENDANCE_FILE = 'attendance.csv'
FAILURE_MSG_ID_NOT_EXIST = 'Invalid ID! Please try again.'
FAILURE_MSG_INVALID_DATETIME = 'Invalid Date or Time! Please try again.'
SUCCESS_MSG = 'Attendance overridden successfully.'

def validate_data(id, date, time_in, time_out):
    """Validates provided user details.
    
    Args:
    id (str): User's unique id.
    date (str): Manual marked date.
    time_in (str): Manual marked time in.
    time_out (str): Manual marked time out.

    Returns:
    bool: Whether the data is valid or not.
    """
    df_registered = pd.read_csv(REGISTERED_USERS_FILE)
    if id not in df_registered['ID'].values:
        messagebox.showinfo('Failure', FAILURE_MSG_ID_NOT_EXIST)
        return False

    try:
        pd.to_datetime(date)
        pd.to_datetime(time_in)
        pd.to_datetime(time_out)
    except ValueError:
        messagebox.showinfo('Failure', FAILURE_MSG_INVALID_DATETIME)
        return False

    return True

def override_attendance():
    """Manually overrides the attendance upon button press."""
    id = id_entry.get()
    date = date_entry.get()
    time_in = time_in_entry.get()
    time_out = time_out_entry.get()

    if validate_data(id, date, time_in, time_out):
        df_attendance = pd.read_csv(ATTENDANCE_FILE)
        df_attendance = df_attendance.append({'ID': id, 'Date': date, 'Time In': time_in, 'Time Out': time_out}, ignore_index=True)
        df_attendance.to_csv(ATTENDANCE_FILE, index=False)
        
        id_entry.delete(0, END)
        date_entry.delete(0, END)
        time_in_entry.delete(0, END)
        time_out_entry.delete(0, END)

        messagebox.showinfo('Success', SUCCESS_MSG)

# Create a window in Tkinter
window = Tk()
window.title("Manual Override")

Label(window, text="User ID").pack()
id_entry = Entry(window)
id_entry.pack()

Label(window, text="Date (YYYY-MM-DD)").pack()
date_entry = Entry(window)
date_entry.pack()

Label(window, text="Time In (HH:MM:SS)").pack()
time_in_entry = Entry(window)
time_in_entry.pack()

Label(window, text="Time Out (HH:MM:SS)").pack()
time_out_entry = Entry(window)
time_out_entry.pack()

Button(window, text="Override Attendance", command=override_attendance).pack()

window.mainloop()
