import cv2
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

class ObjectExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("Object Extractor")
        
        # Controls
        ttk.Button(root, text="Load Image", command=self.load_image).pack(pady=5)
        ttk.Button(root, text="Select ROI", command=self.select_roi).pack(pady=5)
        ttk.Button(root, text="Extract Object", command=self.extract_object).pack(pady=5)
        ttk.Button(root, text="Exit", command=root.quit).pack(pady=5)
        
        # Display
        self.panel = ttk.Label(root)
        self.panel.pack()
        
        self.image = None
        self.roi = None
        self.original_image = None
    
    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if path:
            self.original_image = cv2.imread(path)
            if self.original_image is None:
                messagebox.showerror("Error", "Failed to load image")
                return
                
            self.image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
            self.show_image(self.image)
            self.roi = None
    
    def select_roi(self):
        if self.image is None:
            messagebox.showwarning("Warning", "Please load an image first")
            return
            
        # Create a copy for ROI selection
        temp_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
        
        # Show image and wait for ROI selection
        cv2.namedWindow("Select ROI", cv2.WINDOW_NORMAL)
        cv2.imshow("Select ROI", temp_image)
        
        # Correct ROI selection with proper parameters
        roi = cv2.selectROI("Select ROI", temp_image)
        cv2.destroyAllWindows()
        
        if roi != (0, 0, 0, 0):
            self.roi = roi
            x, y, w, h = roi
            cv2.rectangle(temp_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            self.show_image(temp_image)
    
    def extract_object(self):
        if self.image is None or self.roi is None:
            messagebox.showwarning("Warning", "Please select an ROI first")
            return
            
        x, y, w, h = self.roi
        cropped = self.image[y:y+h, x:x+w]
        
        # Show extracted object in new window
        new_window = tk.Toplevel(self.root)
        new_window.title("Extracted Object")
        
        img = Image.fromarray(cropped)
        img = ImageTk.PhotoImage(img)
        
        panel = ttk.Label(new_window, image=img)
        panel.image = img
        panel.pack()
        
        # Add save button
        ttk.Button(new_window, text="Save Object", 
                  command=lambda: self.save_image(cropped)).pack(pady=5)
    
    def save_image(self, image):
        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
        if path:
            cv2.imwrite(path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
            messagebox.showinfo("Success", "Object saved successfully")
    
    def show_image(self, img):
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img

if __name__ == "__main__":
    root = tk.Tk()
    try:
        app = ObjectExtractor(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        root.destroy()
