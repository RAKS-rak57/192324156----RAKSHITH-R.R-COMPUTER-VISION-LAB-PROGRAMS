import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class UnsharpMaskingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unsharp Masking")
        
        # Controls
        ttk.Button(root, text="Load Image", command=self.load_image).pack()
        ttk.Label(root, text="Blur Amount:").pack()
        self.blur = ttk.Scale(root, from_=1, to=31, value=5)
        self.blur.pack()
        ttk.Label(root, text="Sharpening Amount:").pack()
        self.amount = ttk.Scale(root, from_=0, to=2, value=1)
        self.amount.pack()
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
        mask = cv2.addWeighted(self.image, 1, blurred, -1, 0)
        sharpened = cv2.addWeighted(self.image, 1, mask, self.amount.get(), 0)
        self.show_image(sharpened)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = UnsharpMaskingApp(root)
root.mainloop()
