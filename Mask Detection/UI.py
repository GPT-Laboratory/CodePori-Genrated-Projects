class ApplicationController:
    """
    This class represents the controller in the MVC pattern. It facilitates communication between the model and the view.
    """

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.is_running = False
        self.total_frames = 0
        self.masks_worn = 0
        self.total_temp = 0
        self.attendance_logged = set()

    def start(self):
        self.is_running = True
        self.update()

    def stop(self):
        self.is_running = False

    def update_stats(self, users):
        detected_users = len(users)
        self.total_frames += detected_users
        self.masks_worn += sum(user['mask_worn'] for user in users)
        self.total_temp += sum(user['temp'] for user in users)
        self.attendance_logged.update(user['user_id'] for user in users)

        mask_compliance = f"{self.masks_worn / self.total_frames * 100 : .2f}%" if self.total_frames != 0 else "0%"
        avg_temp = f"{self.total_temp / self.total_frames : .2f}�C" if self.total_frames != 0 else "0�C"
        total_attendance = len(self.attendance_logged)

        self.view.update_stat('Total', self.total_frames)
        self.view.update_stat('Mask Compliance', mask_compliance)
        self.view.update_stat('Average Temperature', avg_temp)
        self.view.update_stat('Total Attendance', total_attendance)

    def update(self):
        if not self.is_running:
            return

        try:
            # Error handling for when a frame could not be read
            ret, frame = self.model.video_capture.read()

            if not ret:
                raise ValueError("Failed to read the frame from video capture")

            frame = self.model.mask_detector.adjust_brightness_contrast(frame)
            detected_users = self.model.mask_detector.detect_and_process(frame)
            self.update_stats(detected_users)

            # Implementation still required: Linking to our 'AttendanceTracker' instance after processing the frame.

            result_frame = self.model.mask_detector.display(frame, detected_users)
            self.view.update_frame(result_frame)

            self.view.master.after(10, self.update)

        except Exception as e:
            # Log error
            print("Error while running the video feed", str(e))
            traceback.print_exc()

            # Display an error messagebox
            tk.messagebox.showerror("Video Feed Error", str(e))

            # Wait for 5 seconds before trying to start the video feed again
            time.sleep(5)
            self.start()
