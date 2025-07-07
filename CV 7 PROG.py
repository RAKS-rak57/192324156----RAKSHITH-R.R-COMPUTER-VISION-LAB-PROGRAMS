import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Webcam Controller")
        
        # Speed controls
        self.speed = 1.0
        ttk.Button(root, text="Slow (0.5x)", command=lambda: self.set_speed(0.5)).pack()
        ttk.Button(root, text="Normal (1x)", command=lambda: self.set_speed(1.0)).pack()
        ttk.Button(root, text="Fast (2x)", command=lambda: self.set_speed(2.0)).pack()
        
        # Webcam display
        self.panel = ttk.Label(root)
        self.panel.pack()
        
        # Open webcam
        self.cap = cv2.VideoCapture(0)
        self.show_frame()
    
    def set_speed(self, speed):
        self.speed = speed
    
    def show_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Adjust frame size based on speed
            if self.speed < 1.0:
                frame = cv2.resize(frame, None, fx=0.7, fy=0.7)
            elif self.speed > 1.0:
                frame = cv2.resize(frame, None, fx=1.3, fy=1.3)
                
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)
            self.panel.config(image=img)
            self.panel.image = img
            
            delay = int(30 / self.speed)  # Adjust delay based on speed
            self.root.after(delay, self.show_frame)
        else:
            self.cap.release()

root = tk.Tk()
app = WebcamApp(root)
root.mainloop()
