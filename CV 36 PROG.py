import cv2
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class WatchDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("Watch Recognition")
        
        # Controls
        ttk.Button(root, text="Load Image", command=self.load_image).pack()
        ttk.Button(root, text="Detect Watch", command=self.detect_watch).pack()
        
        # Display
        self.panel = ttk.Label(root)
        self.panel.pack()
        
        self.image = None
    
    def load_image(self):
        path = filedialog.askopenfilename()
        if path:
            self.image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            self.show_image(self.image)
    
    def detect_watch(self):
        if self.image is None:
            return
            
        # Convert to grayscale
        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        
        # Simple circle detection (for demonstration)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                                 param1=50, param2=30, minRadius=10, maxRadius=100)
        
        img_copy = self.image.copy()
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                cv2.circle(img_copy, (i[0],i[1]), i[2], (0,255,0), 2)
                cv2.putText(img_copy, 'Watch', (i[0]-i[2],i[1]-i[2]),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        
        self.show_image(img_copy)
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

root = tk.Tk()
app = WatchDetector(root)
root.mainloop()
