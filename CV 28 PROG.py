import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class BoundaryDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("Boundary Detection")
        
        # Load image
        self.img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\pedestrian-crossing-sign_hillsboro-oregon_wikimedia.jpg"), cv2.COLOR_BGR2RGB)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        
        # Controls
        ttk.Button(root, text="Find Boundaries", command=self.find_boundaries).pack()
        
        # Display
        self.panel = ttk.Label(root)
        self.panel.pack()
        self.show_image(self.img)
    
    def find_boundaries(self):
        # Edge detection
        edges = cv2.Canny(self.gray, 100, 200)
        
        # Convert to RGB for display
        edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
        self.show_image(edges_rgb)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = BoundaryDetector(root)
root.mainloop()
