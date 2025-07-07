import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def apply_canny():
    edges = cv2.Canny(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 
                     scale1.get(), scale2.get())
    display_image(edges)

root = tk.Tk()
img = cv2.cvtColor(cv2.imread("C:\\Users\RAKSHITH.R.R\Downloads\median-ending.jpg"), cv2.COLOR_BGR2RGB)

ttk.Label(root, text="Threshold 1").pack()
scale1 = ttk.Scale(root, from_=0, to=500, value=100)
scale1.pack()
ttk.Label(root, text="Threshold 2").pack()
scale2 = ttk.Scale(root, from_=0, to=500, value=200)
scale2.pack()
ttk.Button(root, text="Detect Edges", command=apply_canny).pack()

panel = ttk.Label(root)
panel.pack()

def display_image(img):
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img

display_image(img)
root.mainloop()
