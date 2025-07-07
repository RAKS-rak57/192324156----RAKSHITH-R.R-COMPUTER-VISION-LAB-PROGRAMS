import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class DilationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dilation Operation")
        
        # Load image and convert to binary
        self.img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\pedestrian-crossing-sign_hillsboro-oregon_wikimedia.jpg"), cv2.COLOR_BGR2GRAY)
        _, self.binary = cv2.threshold(self.img, 127, 255, cv2.THRESH_BINARY)
        
        # Controls
        ttk.Label(root, text="Kernel Size:").pack()
        self.kernel_size = ttk.Scale(root, from_=1, to=21, value=3, command=self.apply_dilation)
        self.kernel_size.pack()
        
        ttk.Label(root, text="Iterations:").pack()
        self.iterations = ttk.Scale(root, from_=1, to=10, value=1, command=self.apply_dilation)
        self.iterations.pack()
        
        # Display
        self.panel = ttk.Label(root)
        self.panel.pack()
        self.apply_dilation()
    
    def apply_dilation(self, event=None):
        ksize = int(self.kernel_size.get())
        iterations = int(self.iterations.get())
        ksize = ksize if ksize % 2 == 1 else ksize + 1
        kernel = np.ones((ksize, ksize), np.uint8)
        
        dilated = cv2.dilate(self.binary, kernel, iterations=iterations)
        dilated_rgb = cv2.cvtColor(dilated, cv2.COLOR_GRAY2RGB)
        self.show_image(dilated_rgb)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = DilationApp(root)
root.mainloop()
