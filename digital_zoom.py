#Digital zooming (resolution enhancement)

import tkinter as tk
from tkinter import filedialog
import customtkinter
import sys
from PIL import Image, ImageTk
import math
import cv2
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class digital_zooming:
    
    def __init__(self):
        sys.stdout.reconfigure(encoding='utf-8')
        self.root_tk = customtkinter.CTk()
        self.root_tk.title("Digital Zooming")
        self.root_tk.geometry("500x650")
        self.root_tk.resizable(False, False)
        
        self.frame_top = customtkinter.CTkFrame(master=self.root_tk, bg_color="white" , fg_color="white" , height=500)
        self.frame_top.pack(side="top", fill="both",padx=3 ,pady=4)
        
        self.frame_bottom = customtkinter.CTkFrame(master=self.root_tk,  bg_color="gray" ,fg_color="gray")
        self.frame_bottom.pack(side="top", fill="both" , expand=True)
        
        self.file_label = customtkinter.CTkLabel(self.frame_bottom, text="No file selected", fg_color="transparent")
        self.file_label.pack(pady=2)
        self.button = customtkinter.CTkButton(master=self.frame_bottom, text="Browse Image", command=self.browse_file)
        self.button.pack(pady=8)
        
        self.labelZoomSize = customtkinter.CTkLabel(master= self.frame_bottom , text="Zoom Size: 0")
        self.labelZoomSize.pack()
        
        self.slider = customtkinter.CTkSlider(self.frame_bottom ,from_=1, to=10, command=self.slider_event)
        self.slider.pack()
        
        self.image_label = None  # Initialize the image label
        
    def slider_event(self, value):
        zoom_factor = int(math.floor(value))  # Convert the slider value to a float
        print(zoom_factor)
            
    def browse_file(self):
        try:
            self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
            if self.file_path:
                self.display_image(self.file_path)
                self.file_label.configure(text=self.file_path)
            else:
                self.file_label.configure("No file selected")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def display_image(self, file_path):
        try:
            image = Image.open(file_path)
            image = image.resize((500, 500), Image.LANCZOS)  # Resizing the image
            photo = ImageTk.PhotoImage(image)
            if self.image_label:  # Check if an image label already exists
                self.image_label.configure(image=photo, text="")  # Update the image label
            else:
                self.image_label = customtkinter.CTkLabel(self.frame_top, image=photo, text="")
                self.image_label.pack(fill="both", expand=True)
        except Exception as e:
            print(f"An error occurred: {e}")
             
    def zoom(self, image, zoom_factor):
        width, height = image.size
        new_width = int(width * zoom_factor)
        new_height = int(height * zoom_factor)
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        return resized_image      
    def run(self):
        self.root_tk.mainloop()
    
app = digital_zooming()
app.run()



# def digital_zoom(image , zoom_factor):
#     height , width = image.shape[:2]
#     new_height = int(height * zoom_factor)
#     new_width = int(width * zoom_factor)
#     resized_image = cv2.resize(image, (new_width, new_height))
#     return resized_image


# image = cv2.imread('freeren.jpg')

# zoomed_image = digital_zoom(image , 2)

# cv2.imshow('Original Image', image)
# cv2.imshow('Zoomed Image', zoomed_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
