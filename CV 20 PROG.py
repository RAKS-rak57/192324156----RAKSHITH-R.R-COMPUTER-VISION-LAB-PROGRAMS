import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def apply_sharpening():
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=3)
    sharp = gray - 0.5*laplacian
    sharp = np.clip(sharp, 0, 255).astype('uint8')
    display_image(sharp)

root = tk.Tk()
img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\median-ending.jpg"), cv2.COLOR_BGR2RGB)

ttk.Button(root, text="Sharpen", command=apply_sharpening).pack()
panel = ttk.Label(root)
panel.pack()

def display_image(img):
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

display_image(img)
root.mainloop()
