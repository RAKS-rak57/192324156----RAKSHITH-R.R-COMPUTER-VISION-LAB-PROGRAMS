import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class LaplacianDiagonalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Laplacian Sharpening (Diagonal)")
        
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
            
        # Laplacian kernel with diagonal neighbors
        kernel = np.array([[1, 1, 1],
                          [1,-8, 1],
                          [1, 1, 1]])
        
        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        laplacian = cv2.filter2D(gray, -1, kernel)
        sharpened = cv2.addWeighted(gray, 1, laplacian, self.amount.get(), 0)
        sharpened_rgb = cv2.cvtColor(sharpened, cv2.COLOR_GRAY2RGB)
        self.show_image(sharpened_rgb)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = LaplacianDiagonalApp(root)
root.mainloop()
