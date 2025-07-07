import cv2
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import numpy as np

class VehicleDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("Webcam Vehicle Detection")
        
        # Initialize background subtractor
        self.fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
        
        # Controls
        ttk.Label(root, text="Webcam Vehicle Detection", font=('Helvetica', 14)).pack(pady=10)
        
        control_frame = ttk.Frame(root)
        control_frame.pack(pady=10)
        
        ttk.Button(control_frame, text="Start Webcam", command=self.start_webcam).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Stop", command=self.stop_webcam).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Exit", command=root.quit).pack(side=tk.LEFT, padx=5)
        
        # Display
        self.panel = ttk.Label(root)
        self.panel.pack()
        
        self.cap = None
        self.detecting = False
        self.min_contour_area = 1000  # Adjust this for different vehicle sizes
    
    def start_webcam(self):
        if self.detecting:
            return
            
        self.cap = cv2.VideoCapture(0)  # 0 for default webcam
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Could not open webcam")
            return
            
        self.detecting = True
        self.detect_vehicles()
    
    def detect_vehicles(self):
        if not self.detecting:
            return
            
        ret, frame = self.cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to capture frame")
            self.stop_webcam()
            return
            
        # Apply background subtraction
        fgmask = self.fgbg.apply(frame)
        
        # Noise removal
        kernel = np.ones((5,5), np.uint8)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
        
        # Find contours
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw rectangles around moving objects (vehicles)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > self.min_contour_area:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, 'Vehicle', (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Display frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (640, 480))
        
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img
        
        self.root.after(30, self.detect_vehicles)  # ~30fps
    
    def stop_webcam(self):
        self.detecting = False
        if self.cap is not None:
            self.cap.release()
    
    def __del__(self):
        self.stop_webcam()

if __name__ == "__main__":
    root = tk.Tk()
    try:
        app = VehicleDetector(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        root.destroy()
