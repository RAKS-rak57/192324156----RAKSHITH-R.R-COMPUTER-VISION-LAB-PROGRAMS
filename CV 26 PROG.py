import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking")
        
        # Controls
        ttk.Button(root, text="Load Image", command=self.load_image).pack()
        ttk.Button(root, text="Load Watermark", command=self.load_watermark).pack()
        
        ttk.Label(root, text="Opacity:").pack()
        self.opacity = ttk.Scale(root, from_=0, to=100, value=50)
        self.opacity.pack()
        
        ttk.Button(root, text="Apply Watermark", command=self.apply_watermark).pack()
        
        # Display
        self.panel = ttk.Label(root)
        self.panel.pack()
        
        self.image = None
        self.watermark = None
    
    def load_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            self.show_image(self.image)
    
    def load_watermark(self):
        path = filedialog.askopenfilename()
        if path:
            self.watermark = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    
    def apply_watermark(self):
        if self.image is None or self.watermark is None:
            return
            
        # Resize watermark
        h, w = self.image.shape[:2]
        wm = cv2.resize(self.watermark, (w//4, h//4))
        
        # Position at bottom-right
        y_offset = h - wm.shape[0] - 20
        x_offset = w - wm.shape[1] - 20
        
        # Blend
        alpha = self.opacity.get()/100
        overlay = self.image.copy()
        roi = overlay[y_offset:y_offset+wm.shape[0], x_offset:x_offset+wm.shape[1]]
        blended = cv2.addWeighted(roi, 1-alpha, wm[:,:,:3], alpha, 0)
        overlay[y_offset:y_offset+wm.shape[0], x_offset:x_offset+wm.shape[1]] = blended
        
        self.show_image(overlay)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = WatermarkApp(root)
root.mainloop()
