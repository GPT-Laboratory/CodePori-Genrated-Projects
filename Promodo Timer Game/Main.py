import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound  # For sound notifications (Windows only)

# Constants for Pomodoro intervals
DEFAULT_WORK_TIME = 25 * 60  # 25 minutes in seconds
DEFAULT_BREAK_TIME = 5 * 60  # 5 minutes in seconds
DEFAULT_LONG_BREAK_TIME = 15 * 60  # 15 minutes in seconds
POMODORO_CYCLES = 4  # Number of cycles before a long break

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("350x300")

        # Timer configuration
        self.work_time = DEFAULT_WORK_TIME
        self.break_time = DEFAULT_BREAK_TIME
        self.long_break_time = DEFAULT_LONG_BREAK_TIME
        self.is_running = False
        self.is_paused = False
        self.current_cycle = 0
        self.remaining_time = self.work_time

        # Create the timer label
        self.timer_label = tk.Label(root, text="Pomodoro Timer", font=("Arial", 20))
        self.timer_label.pack(pady=10)

        # Create a label to show the countdown
        self.time_label = tk.Label(root, text="25:00", font=("Arial", 30))
        self.time_label.pack(pady=10)

        # Create start, pause/resume, and reset buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=5)

        # Create customization options for work/break time
        self.customize_frame = tk.Frame(root)
        self.customize_frame.pack(pady=10)

        tk.Label(self.customize_frame, text="Work Time (min):").grid(row=0, column=0)
        self.work_time_entry = tk.Entry(self.customize_frame, width=5)
        self.work_time_entry.insert(0, "25")
        self.work_time_entry.grid(row=0, column=1)

        tk.Label(self.customize_frame, text="Break Time (min):").grid(row=1, column=0)
        self.break_time_entry = tk.Entry(self.customize_frame, width=5)
        self.break_time_entry.insert(0, "5")
        self.break_time_entry.grid(row=1, column=1)

        tk.Label(self.customize_frame, text="Long Break Time (min):").grid(row=2, column=0)
        self.long_break_time_entry = tk.Entry(self.customize_frame, width=5)
        self.long_break_time_entry.insert(0, "15")
        self.long_break_time_entry.grid(row=2, column=1)

        self.apply_button = tk.Button(self.customize_frame, text="Apply", command=self.apply_settings)
        self.apply_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Display session tracker
        self.session_tracker = tk.Label(root, text="Completed Sessions: 0", font=("Arial", 12))
        self.session_tracker.pack(pady=10)
        self.completed_sessions = 0

    def apply_settings(self):
        """Apply custom work/break time settings."""
        try:
            self.work_time = int(self.work_time_entry.get()) * 60
            self.break_time = int(self.break_time_entry.get()) * 60
            self.long_break_time = int(self.long_break_time_entry.get()) * 60
            self.remaining_time = self.work_time
            self.update_timer_display(self.remaining_time)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for time settings.")

    def update_timer_display(self, seconds):
        """Update the time display on the GUI."""
        minutes, seconds = divmod(seconds, 60)
        time_formatted = f"{minutes:02d}:{seconds:02d}"
        self.time_label.config(text=time_formatted)

    def start_timer(self):
        """Start the timer."""
        if not self.is_running:
            self.is_running = True
            self.is_paused = False
            self.start_button.config(state=tk.DISABLED)  # Disable start button during running timer
            self.run_timer()

    def run_timer(self):
        """Run the timer in a separate thread."""
        def run():
            while self.is_running and self.remaining_time > 0:
                if not self.is_paused:
                    self.update_timer_display(self.remaining_time)
                    time.sleep(1)
                    self.remaining_time -= 1

            if self.remaining_time == 0:
                self.timer_finished()

        timer_thread = threading.Thread(target=run)
        timer_thread.start()

    def pause_timer(self):
        """Pause or resume the timer."""
        if self.is_paused:
            self.is_paused = False
            self.pause_button.config(text="Pause")
        else:
            self.is_paused = True
            self.pause_button.config(text="Resume")

    def reset_timer(self):
        """Reset the timer and cycle count."""
        self.is_running = False
        self.is_paused = False
        self.remaining_time = self.work_time
        self.update_timer_display(self.remaining_time)
        self.start_button.config(state=tk.NORMAL)  # Re-enable start button
        self.current_cycle = 0
        self.completed_sessions = 0
        self.session_tracker.config(text="Completed Sessions: 0")

    def timer_finished(self):
        """Handle the completion of a timer interval."""
        self.is_running = False
        self.current_cycle += 1
        self.completed_sessions += 1
        self.session_tracker.config(text=f"Completed Sessions: {self.completed_sessions}")

        # Play notification sound
        winsound.Beep(1000, 1000)

        # Long break after a cycle of work sessions
        if self.current_cycle % (POMODORO_CYCLES * 2) == 0:
            messagebox.showinfo("Pomodoro Timer", "Take a long break!")
            self.remaining_time = self.long_break_time
        elif self.current_cycle % 2 == 0:
            messagebox.showinfo("Pomodoro Timer", "Take a short break!")
            self.remaining_time = self.break_time
        else:
            messagebox.showinfo("Pomodoro Timer", "Back to work!")
            self.remaining_time = self.work_time

        self.update_timer_display(self.remaining_time)
        self.start_button.config(state=tk.NORMAL)  # Re-enable start button

# Create the main window for the application
if __name__ == "__main__":
    root = tk.Tk()
    pomodoro_timer = PomodoroTimer(root)
    root.mainloop()
