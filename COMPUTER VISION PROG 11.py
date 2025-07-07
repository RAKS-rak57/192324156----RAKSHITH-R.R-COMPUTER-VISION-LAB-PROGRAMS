import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def apply_transform():
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols,rows))
    display_image(dst)

root = tk.Tk()
img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\JARTECH_Badge.png"), cv2.COLOR_BGR2RGB)
rows,cols = img.shape[:2]

ttk.Button(root, text="Apply Affine", command=apply_transform).pack()
panel = ttk.Label(root)
panel.pack()

def display_image(img):
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

display_image(img)
root.mainloop()
