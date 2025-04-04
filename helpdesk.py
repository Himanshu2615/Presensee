import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
from aboutR import AboutWindow
from system_req import system_req

class HelpDeskApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")
        self.create_buttons()


        

        def open_email(event):
            webbrowser.open("mailto:abhverma45@gmail.com")

        def open_instagram(event):
            webbrowser.open("https://github.com/abhi-456")  # Replace with your Instagram profile URL

        canvas = tk.Canvas(self.root, width=1520, height=790, bg="white")
        canvas.pack()

        # Contact US text
        canvas.create_text(550, 90, text=" Contact Us", font=("times new roman", 45, "bold"), anchor=tk.NW, fill="black")

        # Call icon image
        img1 = Image.open(r".vscode/image x.jpg")
        img1 = img1.resize((120, 100), Image.LANCZOS)
        self.bg1 = ImageTk.PhotoImage(img1)
        canvas.create_image(270, 300, image=self.bg1, anchor=tk.NW)

        # Text
        canvas.create_text(295, 400, text=" Phone", font=("Calibri (Body)", 10, ), anchor=tk.NW, fill="black")
        canvas.create_text(280, 430, text=" 8303727022", font=("Calibri (Body)", 10, ), anchor=tk.NW, fill="black")

        # Add email icon image
        img2 = Image.open(r".vscode/images (1).png")
        img2 = img2.resize((120, 100), Image.LANCZOS)
        self.bg2 = ImageTk.PhotoImage(img2)
        canvas.create_image(660, 300, image=self.bg2, anchor=tk.NW)

        # Text with clickable link (email)
        email_label = tk.Label(canvas, text=" Email", font=("Calibri (Body)", 10, ), anchor=tk.NW, fg="blue", cursor="hand2",bg="white")
        email_label.bind("<Button-1>", open_email)
        canvas.create_window(700, 400, anchor=tk.NW, window=email_label)

        canvas.create_text(650, 430, text=" abhverma45@gmail.com", font=("Calibri (Body)", 10, ), anchor=tk.NW, fill="black")

        # Add Github icon image
        img3 = Image.open(r".vscode/download.jpeg")
        img3 = img3.resize((120, 100), Image.LANCZOS)
        self.bg3 = ImageTk.PhotoImage(img3)
        canvas.create_image(1050, 300, image=self.bg3, anchor=tk.NW)

        # Text with clickable link (GitHub)
        github_label = tk.Label(canvas, text="GitHub", font=("Calibri (Body)", 10,), anchor=tk.NW, fg="blue", cursor="hand2",bg="white")
        github_label.bind("<Button-1>", open_instagram)
        canvas.create_window(1090, 400, anchor=tk.NW, window=github_label)

    def create_buttons(self):
        # Create a frame to encapsulate the button and set its background color
        button_frame = tk.Frame(self.root, bg="#EEDFCC", pady=0)
        button_frame.pack(side=tk.TOP, fill=tk.X)  # Adjust pady values as needed

        # Create an "About Us" button inside the frame
        about_us_button = tk.Button(button_frame, text="About Us", command=self.about, bg="white", fg="black", width=15, height=1)
        about_us_button.pack(side=tk.LEFT, padx=0)

        # Create a "Home" button next to the "About Us" button
        home_button = tk.Button(button_frame, text="Systm Requirment", command=self.req, bg="white", fg="black", width=15, height=1)
        home_button.pack(side=tk.LEFT, padx=0)
    

    def about(self):
        self.new_window= tk.Toplevel(self.root)
        self.app=AboutWindow(self.new_window)

    def req(self):
        self.new_window1= tk.Toplevel(self.root)
        self.app=system_req(self.new_window1)

if __name__ == '__main__':
    root = tk.Tk()
    app = HelpDeskApp(root)
    root.mainloop()
