from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class AboutWindow:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")
        

         # background images
        img=Image.open(r"wall.jpg")
        img=img.resize((1530,790),Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)

        self.canvas = Canvas(self.root, width=1520, height=790)
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
        self.canvas.pack()

        #fl=Label(self.root, image = self.bg)
        #fl.place(x=0,y=0, width = 1530, height=790)

        #canvas = Canvas(self.root, width=1520, height=790)
        #canvas.pack()
          # Add description text on the canvas without a background

         # ABOUT US text
        #label3 = Label(self.root, text=" ABOUT US ", font=("Calibri (Body)", 45, "bold"))
        #label3.place(x=900, y=50)

         # Create text on the canvas
        self.canvas.create_text(900, 70, text=" About US", font=("times new romans", 45, "bold"), anchor=NW, fill="black")

        description = '''Our Face Recognition Attendance System
is a cutting-edge
Python-based application designed to streamline
attendance tracking.
Leveraging state-of-the-art facial recognition
technology,
this system offers a convenient and secure way to
automate attendance management.
With its user-friendly interface and
robust features,
our system ensures accurate attendance records,
simplifies administrative tasks, and
enhances efficiency
in various educational or corporate settings.'''

        

        # Create text on the canvas
        self.canvas.create_text(900, 200, text=description, font=("Calibri (Body)", 15, "bold"), anchor=NW, fill="black")





if __name__ == '__main__':
    root = Tk()
    app = AboutWindow(root)
    root.mainloop()       