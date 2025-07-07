import cv2
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class FaceDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Detection")
        
        # Load classifier
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Controls
        ttk.Button(root, text="Load Image", command=self.load_image).pack()
        ttk.Button(root, text="Detect Faces", command=self.detect_faces).pack()
        
        # Display
        self.panel = ttk.Label(root)
        self.panel.pack()
        
        self.image = None
    
    def load_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            self.show_image(self.image)
    
    def detect_faces(self):
        if self.image is None:
            return
            
        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        img_with_faces = self.image.copy()
        for (x,y,w,h) in faces:
            cv2.rectangle(img_with_faces, (x,y), (x+w,y+h), (255,0,0), 2)
        
        self.show_image(img_with_faces)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = FaceDetector(root)
root.mainloop()
