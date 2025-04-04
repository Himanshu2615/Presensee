import cv2
import os
import threading
import time
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import face_recognition

class CameraCapture:
    def __init__(self, save_path, capture_count, window):
        self.vid = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.save_path = save_path
        self.capture_count = capture_count
        self.image_count = 1
        self.capture_interval = 5  # in seconds

        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        self.window = window
        self.canvas = tk.Canvas(self.window, width=self.vid.get(3), height=self.vid.get(4))
        self.canvas.pack()

        self.known_faces = self.load_known_faces()  # Load known faces and their encodings

        self.capture_thread = threading.Thread(target=self.start_capture)
        self.capture_thread.start()

        self.update_thread = threading.Thread(target=self.update)
        self.update_thread.start()

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        return frame

    def load_known_faces(self):
        known_faces_folder = "known_faces"
        known_faces = []

        if not os.path.exists(known_faces_folder):
            os.makedirs(known_faces_folder)

        for filename in os.listdir(known_faces_folder):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                name = os.path.splitext(filename)[0][:-1]
                image_path = os.path.join(known_faces_folder, filename)
                image = face_recognition.load_image_file(image_path)
                face_encoding = face_recognition.face_encodings(image)[0]
                known_faces.append((name, face_encoding))

        return known_faces

    def recognize_faces(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        recognized_names = []

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            name = "Unknown"
            min_distance = float("inf")

            for known_name, known_encoding in self.known_faces:
                distance = face_recognition.face_distance([known_encoding], face_encoding)[0]

                if distance < min_distance:
                    min_distance = distance
                    name = known_name

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
            recognized_names.append((name, min_distance))

        return frame, recognized_names

    def save_image(self, frame):
        frame_with_faces = self.detect_faces(frame)
        gray_frame = cv2.cvtColor(frame_with_faces, cv2.COLOR_BGR2GRAY)
        image_filename = os.path.join(self.save_path, f"image_{self.image_count}.png")
        variance = np.var(gray_frame)

        if variance > 100:
            cv2.imwrite(image_filename, gray_frame)
            self.image_count += 1
            print(f"Image saved as {image_filename}")
            frame_with_recognition, recognized_names = self.recognize_faces(frame)
            self.log_recognition_results(image_filename, recognized_names)
        else:
            print("Skipping image (potential fake)")

    def log_recognition_results(self, image_filename, recognized_names):
        if recognized_names != "unknown":
            df = pd.DataFrame({"Image Filename": [image_filename],
                               "Recognized Names": [", ".join([name for name, _ in recognized_names])],
                               "Similarity Scores": [", ".join([f"{score:.2f}" for _, score in recognized_names])]})
            if not os.path.exists("recognition_log.csv"):
                df.to_csv("recognition_log.csv", index=False)
            else:
                df.to_csv("recognition_log.csv", mode="a", header=False, index=False)

    def start_capture(self):
        start_time = time.time()

        while self.image_count <= self.capture_count:
            ret, frame = self.vid.read()
            if ret:
                current_time = time.time()
                if current_time - start_time >= self.capture_interval:
                    self.save_image(frame)
                    start_time = current_time

        self.vid.release()
        print("Image capture completed.")

    def update(self):
        while True:
            ret, frame = self.vid.read()
            if ret:
                frame_with_faces = self.detect_faces(frame)
                frame_with_recognition, recognized_names = self.recognize_faces(frame_with_faces)

                # Display recognized names and similarity scores
                font = cv2.FONT_HERSHEY_DUPLEX
                y = 30
                for name, score in recognized_names:
                    cv2.putText(frame_with_recognition, f'Name: {name}', (10, y), font, 0.5, (0, 0, 0), 1)
                    cv2.putText(frame_with_recognition, f'Similarity: {100 - score * 100:.2f}%', (10, y + 20), font, 0.5, (0, 0, 0), 1)
                    y += 50

                photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame_with_recognition, cv2.COLOR_BGR2RGB)))
                self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
                self.canvas.photo = photo  # Keep a reference to prevent garbage collection

# Specify the path to save images and the number of images to capture
if __name__ == '__main__':
    save_path = "test_images"
    capture_count = 1
    root = tk.Tk()
    root.title("Camera_App")
    app = CameraCapture(save_path, capture_count, root)
    root.mainloop()
