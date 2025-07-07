import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class HighBoostApp:
    def __init__(self, root):
        self.root = root
        self.root.title("High-Boost Masking")
        
        # Controls
        ttk.Button(root, text="Load Image", command=self.load_image).pack()
        ttk.Label(root, text="Blur Amount:").pack()
        self.blur = ttk.Scale(root, from_=1, to=31, value=5)
        self.blur.pack()
        ttk.Label(root, text="Boost Factor (A):").pack()
        self.boost = ttk.Scale(root, from_=1, to=3, value=1.5)
        self.boost.pack()
        ttk.Button(root, text="Apply", command=self.apply_sharpening).pack()
        
        # Display
        self.panel = ttk.Label(root)
        self.panel.pack()
        self.image = None
    
    def load_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            self.show_image(self.image)
    
    def apply_sharpening(self):
        if self.image is None:
            return
            
        # Get odd blur size
        ksize = int(self.blur.get())
        ksize = ksize if ksize % 2 == 1 else ksize + 1
        
        blurred = cv2.GaussianBlur(self.image, (ksize, ksize), 0)
        mask = cv2.addWeighted(self.image, self.boost.get(), blurred, -1, 0)
        sharpened = cv2.addWeighted(self.image, 1, mask, 1, 0)
        self.show_image(sharpened)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = HighBoostApp(root)
root.mainloop()
