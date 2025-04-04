import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tryspacy import ChatBot 
from helpdesk import HelpDeskApp
from Project import CameraCapture
import datetime
import pyttsx3
import cv2
import face_recognition_module as frm

class FaceIdentificationSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Identification System")
        self.create_main_window()
        self.current_language = "en_US"  
        self.create_buttons()
        self.create_language_selector()
        self.update_time()
        


    def create_main_window(self):
        bg_img = Image.open(r"bg117.webp")
        bg_img = bg_img.resize((1530, 790), Image.BILINEAR)
        self.bg_photoimg = ImageTk.PhotoImage(bg_img)
        background_label = tk.Label(self.root, image=self.bg_photoimg)
        background_label.place(x=0, y=0, width=1530, height=790)
    def create_buttons(self):
        translations = {
            "Student Details": {
                "en_US": "Student Details",
                "hi_IN": "छात्र विवरण"
            },
            "Face Detector": {
                "en_US": "Face Detector",
                "hi_IN": "चेहरा डिटेक्टर"
            },
            "Attendance": {
                "en_US": "Attendance",
                "hi_IN": "उपस्थिति"
            },
            "Train Data": {
                "en_US": "Train Data",
                "hi_IN": "डेटा प्रशिक्षित करें"
            },
            "Photos": {
                "en_US": "Photos",
                "hi_IN": "तस्वीरें"
            },
            "Help": {
                "en_US": "Help",
                "hi_IN": "मदद"
            },
            "Chat-Bot": {
                "en_US": "Chat-Bot",
                "hi_IN": "चैट बॉट"
            }
        }

        button_data = [
            #("Student Details", self.open_student_details),
            ("Face Detector", self.open_face_detector),
            #("Attendance", self.open_attendance),
            #("Train Data", self.open_train_data),
            #("Photos", self.open_photos),
            ("Help", self.open_help),
            ("Chat-Bot", self.open_Chat_Bot)
        ]

        for idx, (text, command_func) in enumerate(button_data):
            translated_text = translations.get(text, {}).get(self.current_language, text)
            button = tk.Button(
                self.root,
                text=translated_text,
                cursor="hand2",
                command=lambda func=command_func, txt=text: self.on_button_click(func, txt),   
                bg="#E2E2B6",
                activebackground="orange",
                font=("calibri", 15, "bold"),
                fg="white"
            )
            button.place(x=0, y=200 + idx * 70, width=275, height=45)

    def update_time(self):
        def update():
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%H:%M:%S  %Y-%m-%d")
            time_label.config(text="Time:- " + formatted_time)
            self.root.after(1000, update)

        time_label = tk.Label(self.root, font=("Helvetica", 16, "bold"), fg="white", bg="black")
        time_label.place(x=1175, y=700)
        update()  

    def create_language_selector(self):
        self.language_var = tk.StringVar(self.root)
        language_choices = ["English (US)", "Hindi (IN)"]
        self.language_selector = ttk.Combobox(self.root, textvariable=self.language_var, values=language_choices)
        self.language_selector.place(x=1250, y=50)
        self.language_selector.set("English (US)")
        self.language_selector.bind("<<ComboboxSelected>>", self.change_language)

    def change_language(self, event):
        selected_language = self.language_var.get()
        if selected_language == "Hindi (IN)":
            self.current_language = "hi_IN"
        else:
            self.current_language = "en_US"
        self.create_buttons()

    def on_button_click(self, command_func, text):
        
        if callable(command_func):
            command_func()

        
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    #def open_student_details(self):
        #self.student_window = tk.Toplevel(self.root)
        #self.student_app = Student(self.student_window)

    def open_face_detector(self):
        self.face_detector_window = tk.Toplevel(self.root)
        self.face_detector_label = tk.Label(self.face_detector_window, text="Face Detector", font=("Helvetica", 16))
        self.face_detector_label.pack()
        
        self.start_detector_button = tk.Button(self.face_detector_window, text="Start Face Detection", command=self.start_face_detection)
        self.start_detector_button.pack()

    def start_face_detection(self):
        dataset_path = "images"
        known_faces, known_names, known_ids = frm.train_face_recognition(dataset_path)

        video_capture = cv2.VideoCapture(0)
        attendance_filename = f"attendance_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv"
        marked_attendance = set()

        while True:
            ret, frame = video_capture.read()
            result_frame = frm.recognize_faces(known_faces, known_names, known_ids, frame, marked_attendance, attendance_filename)

            cv2.imshow('Face Recognition Attendance System', result_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

    #def open_attendance(self):
        #self.attendance_window = tk.Toplevel(self.root)
        

    #def open_train_data(self):
        #self.train_data_window = tk.Toplevel(self.root)


    #def open_photos(self):
        #self.photos_window = tk.Toplevel(self.root)
        #self.photos_app = DirectoryOpener("./known_faces")
        #self.photos_app.open_directory_in_file_explorer()

    def open_Chat_Bot(self):
        self.ChatBot_window = tk.Toplevel(self.root)
        self.ChatBot_app = ChatBot(self.ChatBot_window)

    def open_help(self):
        self.help_window = tk.Toplevel(self.root)
        self.help_window_app = HelpDeskApp(self.help_window)  

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceIdentificationSystem(root)
    root.mainloop()
