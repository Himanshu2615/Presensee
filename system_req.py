from tkinter import*
import tkinter as tk
from tkinter import ttk

class system_req:
    def __init__(self,root):
        self.root = root
        self.root.geometry("790x680+0+0")
        self.root.title("system_requirment")

        canvas = tk.Canvas(self.root, width=790, height=680, bg="white")
        canvas.pack()

        canvas.create_text(10, 20, text=" Hardware Requirment ", font=("times new roman", 20, "bold"), anchor=tk.NW, fill="black")
        canvas.create_text(20, 55, text=" Processor (CPU): ", font=("times new roman", 15, "bold"), anchor=tk.NW, fill="black")
        des1=  '''   A multi-core processor (quad-core or higher) is recommended
   for handling image processing tasks efficiently.'''
        canvas.create_text(20, 85, text=des1 , font=("times new roman", 11, ), anchor=tk.NW, fill="black")
        canvas.create_text(20, 130, text=" Memory (RAM): ", font=("times new roman", 15, "bold"), anchor=tk.NW, fill="black")
        canvas.create_text(30, 160, text=" At least 8 GB of RAM is recommended ", font=("times new roman", 11, ), anchor=tk.NW, fill="black")

        
        
        canvas.create_text(10, 200, text=" Software Requirment ", font=("times new roman", 20, "bold"), anchor=tk.NW, fill="black")
        canvas.create_text(20, 235, text=" Operating System:", font=("times new roman", 15, "bold"), anchor=tk.NW, fill="black")
        canvas.create_text(30, 265, text=" Windows 10 is required" , font=("times new roman", 11, ), anchor=tk.NW, fill="black")

        canvas.create_text(20, 285, text=" Python and Libraries:", font=("times new roman", 15, "bold"), anchor=tk.NW, fill="black")
        

        des='''Install the latest version of Python.
    Required Python libraries/modules:
    Tkinter
    OpenCV
    Pymysql
    Pillow
    SQL
'''
        canvas.create_text(30, 305, text=des , font=("times new roman", 11, ), anchor=tk.NW, fill="black")







if __name__ == '__main__':
    root = Tk()
    app = system_req(root)
    root.mainloop()       