import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageMover:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Mover")
        
        # Load image
        self.img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\median-ending.jpg"), cv2.COLOR_BGR2RGB)
        self.x, self.y = 100, 100
        
        # Movement controls
        ttk.Button(root, text="Move Left", command=lambda: self.move_image(-20, 0)).pack(side=tk.LEFT)
        ttk.Button(root, text="Move Right", command=lambda: self.move_image(20, 0)).pack(side=tk.LEFT)
        ttk.Button(root, text="Move Up", command=lambda: self.move_image(0, -20)).pack(side=tk.LEFT)
        ttk.Button(root, text="Move Down", command=lambda: self.move_image(0, 20)).pack(side=tk.LEFT)
        
        # Canvas for movement
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()
        
        # Display initial image
        self.img_tk = ImageTk.PhotoImage(Image.fromarray(self.img))
        self.image_on_canvas = self.canvas.create_image(self.x, self.y, image=self.img_tk)
    
    def move_image(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.coords(self.image_on_canvas, self.x, self.y)

root = tk.Tk()
app = ImageMover(root)
root.mainloop()
