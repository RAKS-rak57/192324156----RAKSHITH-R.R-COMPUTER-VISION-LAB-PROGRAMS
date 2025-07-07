import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class GradientMaskingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gradient Masking")
        
        # Controls
        ttk.Button(root, text="Load Image", command=self.load_image).pack()
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
            
        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        gradient = np.sqrt(sobelx**2 + sobely**2)
        gradient = np.uint8(255 * gradient / np.max(gradient))
        
        sharpened = cv2.addWeighted(self.image, 1, 
                                  cv2.cvtColor(gradient, cv2.COLOR_GRAY2RGB), 
                                  self.amount.get(), 0)
        self.show_image(sharpened)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = GradientMaskingApp(root)
root.mainloop()
