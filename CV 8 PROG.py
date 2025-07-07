import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageScaler:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Scaler")
        
        # Load image
        self.img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\median-ending.jpg"), cv2.COLOR_BGR2RGB)
        self.original = self.img.copy()
        
        # Scale controls
        ttk.Label(root, text="Scale Factor:").pack()
        self.scale = ttk.Scale(root, from_=50, to=200, command=self.update_image)
        self.scale.set(100)
        self.scale.pack()
        
        # Image display
        self.panel = ttk.Label(root)
        self.panel.pack()
        self.update_image()
    
    def update_image(self, event=None):
        scale_factor = self.scale.get() / 100
        h, w = self.original.shape[:2]
        resized = cv2.resize(self.original, (int(w*scale_factor), int(h*scale_factor)))
        
        img = Image.fromarray(resized)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = ImageScaler(root)
root.mainloop()
