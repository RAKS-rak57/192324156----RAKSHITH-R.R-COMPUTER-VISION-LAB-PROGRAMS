import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class ImageCompositor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Compositor")
        
        # Controls
        ttk.Button(root, text="Load Base Image", command=self.load_base).pack()
        ttk.Button(root, text="Load Overlay Image", command=self.load_overlay).pack()
        ttk.Button(root, text="Paste Overlay", command=self.paste_overlay).pack()
        
        # Display
        self.panel = ttk.Label(root)
        self.panel.pack()
        
        self.base = None
        self.overlay = None
    
    def load_base(self):
        path = filedialog.askopenfilename()
        if path:
            self.base = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            self.show_image(self.base)
    
    def load_overlay(self):
        path = filedialog.askopenfilename()
        if path:
            self.overlay = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    
    def paste_overlay(self):
        if self.base is None or self.overlay is None:
            return
            
        # Resize overlay to 25% of base
        h, w = self.base.shape[:2]
        overlay_resized = cv2.resize(self.overlay, (w//4, h//4))
        
        # Position at center
        y_offset = h//2 - overlay_resized.shape[0]//2
        x_offset = w//2 - overlay_resized.shape[1]//2
        
        # Composite
        composite = self.base.copy()
        composite[y_offset:y_offset+overlay_resized.shape[0], 
                 x_offset:x_offset+overlay_resized.shape[1]] = overlay_resized
        
        self.show_image(composite)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = ImageCompositor(root)
root.mainloop()
