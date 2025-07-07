import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class DilationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Dilation")
        
        # Load image
        self.original_img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\median-ending.jpg"), cv2.COLOR_BGR2RGB)
        self.gray_img = cv2.cvtColor(self.original_img, cv2.COLOR_RGB2GRAY)
        
        # Create controls
        ttk.Label(root, text="Kernel Size:").pack()
        self.kernel_size = ttk.Scale(root, from_=1, to=21, value=3, command=self.update_dilation)
        self.kernel_size.pack()
        
        ttk.Label(root, text="Iterations:").pack()
        self.iterations = ttk.Scale(root, from_=1, to=10, value=1, command=self.update_dilation)
        self.iterations.pack()
        
        # Image display
        self.panel = ttk.Label(root)
        self.panel.pack()
        
        self.update_dilation()
    
    def update_dilation(self, event=None):
        ksize = int(self.kernel_size.get())
        iterations = int(self.iterations.get())
        
        # Ensure kernel size is odd
        ksize = ksize if ksize % 2 == 1 else ksize + 1
        
        kernel = np.ones((ksize, ksize), np.uint8)
        dilated = cv2.dilate(self.gray_img, kernel, iterations=iterations)
        
        # Convert back to RGB for display
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
