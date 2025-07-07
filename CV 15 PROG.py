import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def apply_dlt():
    src_pts = np.float32([[50,50],[200,50],[200,200],[50,200]])
    dst_pts = np.float32([[30,100],[220,40],[220,220],[50,250]])
    H = cv2.getPerspectiveTransform(src_pts, dst_pts)
    dst = cv2.warpPerspective(img, H, (cols,rows))
    display_image(dst)

root = tk.Tk()
img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\median-ending.jpg"), cv2.COLOR_BGR2RGB)
rows,cols = img.shape[:2]

ttk.Button(root, text="Apply DLT", command=apply_dlt).pack()
panel = ttk.Label(root)
panel.pack()

def display_image(img):
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

display_image(img)
root.mainloop()
