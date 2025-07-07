import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class OpeningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Opening Operation")
        
        # Load image and convert to binary
        self.img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\pedestrian-crossing-sign_hillsboro-oregon_wikimedia.jpg"), cv2.COLOR_BGR2GRAY)
        _, self.binary = cv2.threshold(self.img, 127, 255, cv2.THRESH_BINARY)
        
        # Controls
        ttk.Label(root, text="Kernel Size:").pack()
        self.kernel_size = ttk.Scale(root, from_=1, to=21, value=3, command=self.apply_opening)
        self.kernel_size.pack()
        
        # Display
        self.panel = ttk.Label(root)
        self.panel.pack()
        self.apply_opening()
    
    def apply_opening(self, event=None):
        ksize = int(self.kernel_size.get())
        ksize = ksize if ksize % 2 == 1 else ksize + 1
        kernel = np.ones((ksize, ksize), np.uint8)
        
        opened = cv2.morphologyEx(self.binary, cv2.MORPH_OPEN, kernel)
        opened_rgb = cv2.cvtColor(opened, cv2.COLOR_GRAY2RGB)
        self.show_image(opened_rgb)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = OpeningApp(root)
root.mainloop()
