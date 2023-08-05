import tkinter as tk
import time
from PIL import Image, ImageTk
import os

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automatic Attendance Maker")

        self.camera_label = tk.Label(root)
        self.camera_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_capture)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_capture)
        self.stop_button.pack()

        self.capture_active = False

    def start_capture(self):
        self.capture_active = True
        self.capture_images()

    def stop_capture(self):
        self.capture_active = False

    def capture_images(self):
        while self.capture_active:
            # Get timestamp
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

            # Capture image (placeholder)
            # You might need to replace this with actual camera capture code
            # For example: camera_capture = capture_from_camera()
            camera_capture = Image.new("RGB", (640, 480), "white")

            # Save image with timestamp
            image_filename = f"attendance_{timestamp}.png"
            camera_capture.save(image_filename)

            # Display captured image on the GUI
            img = ImageTk.PhotoImage(camera_capture)
            self.camera_label.config(image=img)
            self.camera_label.image = img

            # Delay before capturing the next image
            time.sleep(5)  # Adjust this delay as needed

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
