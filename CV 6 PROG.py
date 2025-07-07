import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        
        # Video controls
        self.speed = 1.0
        ttk.Button(root, text="Slow (0.5x)", command=lambda: self.set_speed(0.5)).pack()
        ttk.Button(root, text="Normal (1x)", command=lambda: self.set_speed(1.0)).pack()
        ttk.Button(root, text="Fast (2x)", command=lambda: self.set_speed(2.0)).pack()
        
        # Video display
        self.panel = ttk.Label(root)
        self.panel.pack()
        
        # Open video file
        self.cap = cv2.VideoCapture("D:\\CN ARP PROTOCOL TRAFFIC SIMULATION CISCO .mp4")
        self.play_video()
    
    def set_speed(self, speed):
        self.speed = speed
    
    def play_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 480))
            
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)
            self.panel.config(image=img)
            self.panel.image = img
            
            delay = int(25 / self.speed)  # Adjust delay based on speed
            self.root.after(delay, self.play_video)
        else:
            self.cap.release()

root = tk.Tk()
app = VideoPlayer(root)
root.mainloop()
