import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageRotator:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Rotator")
        
        # Load image
        self.img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\median-ending.jpg"), cv2.COLOR_BGR2RGB)
        self.angle = 0
        
        # Rotation controls
        ttk.Button(root, text="Rotate 90° CW", command=lambda: self.rotate_image(90)).pack()
        ttk.Button(root, text="Rotate 90° CCW", command=lambda: self.rotate_image(-90)).pack()
        
        # Image display
        self.panel = ttk.Label(root)
        self.panel.pack()
        self.show_image()
    
    def rotate_image(self, angle):
        self.angle += angle
        h, w = self.img.shape[:2]
        center = (w//2, h//2)
        M = cv2.getRotationMatrix2D(center, self.angle, 1.0)
        rotated = cv2.warpAffine(self.img, M, (w, h))
        self.show_image(rotated)
    
    def show_image(self, img=None):
        display_img = self.img if img is None else img
        img = Image.fromarray(display_img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = ImageRotator(root)
root.mainloop()
