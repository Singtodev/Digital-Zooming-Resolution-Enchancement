import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

# สร้างฟังก์ชันเพื่อดึงรูปภาพจากเครื่องซึ่งจะได้ filePath
def browseImage():
    return filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
# สร้าง class digitalZoomApp
class DigitalZoomApp:
    
    # constructor
    def __init__(self, master, image_path):
        
        # กำหนดตัว แปล panel
        self.master = master
        self.master.title("Digital Zoom")
        self.image = Image.open(image_path)
        # ดึงขนาดรูปภาพที่รับเข้ามา
        self.width, self.height = self.image.size
        
        # กำหนด factors
        self.zoom_factor = 1.0
        self.pan_x_factor = 0
        self.pan_y_factor = 0
        
        # สร้าง frame ที่มีขนาด เท่าไซด์รูปภาพ
        self.canvas = tk.Canvas(master, width=self.width, height=self.height)
        self.canvas.pack()
        
        # เรียก update image เพื่อ show รูปภาพ
        self.update_image()
        
        #สร้าง frame panel สำหรับ menu zoom in , zoom out
        self.frame_bottom = tk.Frame(master=master , background=master["bg"])
        self.frame_bottom.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        
        #สร้าง frame panel สำหรับ controls menu
        self.frame_bottom1 = tk.Frame(master=master , background=master["bg"])
        self.frame_bottom1.place(relx=0.5, rely=0.90, anchor=tk.CENTER)
        
        # zoom in button
        self.zoom_in_button = tk.Button(self.frame_bottom, text="Zoom In +", command=self.zoom_in)
        self.zoom_in_button.pack(side=tk.LEFT, padx=5)
        
        # zoom out button
        self.zoom_out_button = tk.Button(self.frame_bottom, text="Zoom Out -", command=self.zoom_out)
        self.zoom_out_button.pack(side=tk.LEFT, padx=5)
        
        # controls left , right , up , down button
        self.pan_left_button = tk.Button(self.frame_bottom1, text="Pan Left", command=self.pan_left)
        self.pan_left_button.pack(side=tk.LEFT, padx=5)
        
        self.pan_right_button = tk.Button(self.frame_bottom1, text="Pan Right", command=self.pan_right)
        self.pan_right_button.pack(side=tk.LEFT, padx=5)
        
        self.pan_up_button = tk.Button(self.frame_bottom1, text="Pan Up", command=self.pan_up)
        self.pan_up_button.pack(side=tk.LEFT, padx=5)
        
        self.pan_down_button = tk.Button(self.frame_bottom1, text="Pan Down", command=self.pan_down)
        self.pan_down_button.pack(side=tk.LEFT, padx=5)
        
        self.center_button = tk.Button(self.frame_bottom1, text="Center Image", command=self.center_image)
        self.center_button.pack(side=tk.LEFT, padx=5)
        
    def update_image(self):
        # คำนวน zoom
        zoomed_image = self.image.resize(self.calculate_zoomed_size())
        #เมื่อได้รับข้อมูลแล้วแปลงเป็น image
        self.tk_image = ImageTk.PhotoImage(zoomed_image)
        # เครียร์ข้อมูล ใน canvas ออกให้หมด แล้วใส่รูปภาพใหม่เข้าไป และ คำนวน ค่า factor pan กล้อง 
        self.canvas.delete("all")  # Clear previous image
        self.canvas.create_image(-self.pan_x_factor, -self.pan_y_factor, anchor=tk.NW, image=self.tk_image)

    def calculate_zoomed_size(self):
        # คำนวน width , height ใหม่ด้วย ค่า factor
        new_width = int(self.width * self.zoom_factor)
        new_height = int(self.height * self.zoom_factor)
        # และส่งข้อมูลกลับไป
        return new_width, new_height
        
    def zoom_in(self):
        # ซูมเข้าไป
        self.zoom_factor += 0.4
        self.update_image()
        
    def pan_left(self):
        # ปรับมุมกล้องไปทางซ้าย
        self.pan_x_factor -= 40
        self.update_image()
        
    def pan_right(self):
        # ปรับมุมกล้องไปทางขวา
        self.pan_x_factor += 40
        self.update_image()
        
    def pan_up(self):
        # ปรับมุมกล้องไปข้างบน
        self.pan_y_factor -= 40
        self.update_image()
        
    def pan_down(self):
        # ปรับมุมกล้องไปข้างล่าง
        self.pan_y_factor += 40
        self.update_image()
        
    def center_image(self):
        # ปรับรูปภาพให้เหมือนเดิม
        self.pan_x_factor = 0
        self.pan_y_factor = 0
        self.zoom_factor = 1.0
        self.update_image()
        
        
    def zoom_out(self):
        # ซูมออก
        self.zoom_factor -= 0.4
        if self.zoom_factor < 0.4:
            self.zoom_factor = 0.4  # Set a minimum zoom factor to prevent zooming out too much
        self.update_image()
        
def main():
    # เมื่่อเริ่ม app ให้ดึง file path จากเครื่องมา 1 รูป
    image_path = browseImage()
    # ถ้าดึงได้จริงจะทำการสร้าง panel ด้วย tkinter และ ส่ง main panel ไปยัง class digitalzoom app
    if image_path:
        root = tk.Tk()
        app = DigitalZoomApp(root, image_path)
        root.mainloop()

if __name__ == "__main__":
    main()
