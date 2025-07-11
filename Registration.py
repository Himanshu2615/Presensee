import os.path
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import util

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+100+120")

        self.register_new_user_button_main_window = util.get_button(self.main_window, "Register New User", "green", self.register_new_user, fg="black")
        self.register_new_user_button_main_window.place(x=850, y=300)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

        self.db_dir = "./known_faces"
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame

        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)

        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)

        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(10, self.process_webcam)

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+120+140")

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, "Register", "green", self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=850, y=300)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, "Try Again", "red", self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=850, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window, "Please, \nInput username: ")
        self.text_label_register_new_user.place(x=750, y=70)

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def accept_register_new_user(self):
        name = str(self.entry_text_register_new_user.get(1.0, 'end-1c'))

        cv2.imwrite(os.path.join(self.db_dir, "{}.jpg".format(name)), self.register_new_user_capture)

        util.msg_box("Success!", "User was successfully registered")

        self.register_new_user_window.destroy()

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def start(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
