import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def transform_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pts1 = np.float32([[50,50],[200,50],[50,200],[200,200]])
        pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(frame, M, (300,300))
        display_image(dst)
    root.after(10, transform_frame)

root = tk.Tk()
cap = cv2.VideoCapture(0)

panel = ttk.Label(root)
panel.pack()

def display_image(img):
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

transform_frame()
root.mainloop()
cap.release()
