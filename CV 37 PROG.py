import cv2
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import numpy as np

class ReverseVideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Reverse Video Player")
        
        # Video controls
        ttk.Button(root, text="Load Video", command=self.load_video).pack(pady=5)
        ttk.Button(root, text="Play Reverse", command=self.play_reverse).pack(pady=5)
        ttk.Button(root, text="Stop", command=self.stop_video).pack(pady=5)
        ttk.Button(root, text="Exit", command=root.quit).pack(pady=5)
        
        # Video display
        self.panel = ttk.Label(root)
        self.panel.pack()
        
        self.cap = None
        self.frames = []
        self.playing = False
        self.current_frame = 0
    
    def load_video(self):
        path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.avi *.mov"), ("All files", "*.*")])
        if path:
            self.cap = cv2.VideoCapture(path)
            self.frames = []
            self.playing = False
            self.current_frame = 0
            
            # Read all frames
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break
                self.frames.append(frame)
            
            if self.frames:
                self.show_frame(len(self.frames)-1)
            else:
                print("Error: Could not read video frames")
            self.cap.release()
    
    def play_reverse(self):
        if not self.frames:
            print("No video loaded!")
            return
            
        self.playing = True
        self.current_frame = len(self.frames) - 1
        self._update_reverse()
    
    def _update_reverse(self):
        if not self.playing or self.current_frame < 0:
            return
            
        self.show_frame(self.current_frame)
        self.current_frame -= 1
        self.root.after(30, self._update_reverse)  # ~30fps
    
    def show_frame(self, idx):
        frame = cv2.cvtColor(self.frames[idx], cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (640, 480))
        
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img
    
    def stop_video(self):
        self.playing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = ReverseVideoPlayer(root)
    root.mainloop()
