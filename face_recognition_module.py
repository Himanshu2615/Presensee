import time
import cv2
import face_recognition
import os
import joblib
import csv
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def extract_info_from_filename(filename):
    parts = os.path.splitext(filename)[0].split('_')
    if len(parts) == 3:
        name, emp_id, image_no = parts
        return name, emp_id
    else:
        return None, None

def train_face_recognition(dataset_path, model_save_path="trained_model.joblib"):
    start_time = time.time()
    known_faces = []
    known_names = []
    known_ids = []

    if os.path.exists(model_save_path):
        print("Loading pre-trained model...")
        known_faces, known_names, known_ids = joblib.load(model_save_path)
        return known_faces, known_names, known_ids

    print("Training the model...")

    def resize_image(image):
        return cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    def process_image(image_path):
        image = face_recognition.load_image_file(image_path)
        image = resize_image(image)
        face_landmarks = face_recognition.face_landmarks(image)

        if face_landmarks:
            top, right, bottom, left = face_recognition.face_locations(image)[0]
            face_encoding = face_recognition.face_encodings(image, [(top, right, bottom, left)])[0]
            name, emp_id = extract_info_from_filename(os.path.basename(image_path))
            known_faces.append(face_encoding)
            known_names.append(name)
            known_ids.append(emp_id)
        else:
            print(f"No face detected in {image_path}")

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        for person_name in os.listdir(dataset_path):
            person_path = os.path.join(dataset_path, person_name)

            if os.path.isdir(person_path):
                image_paths = [os.path.join(person_path, image_name) for image_name in os.listdir(person_path)]
                executor.map(process_image, image_paths)

    joblib.dump((known_faces, known_names, known_ids), model_save_path)
    print("Finished")
    print("Model took", time.time() - start_time, "seconds")

    return known_faces, known_names, known_ids

def recognize_faces(known_faces, known_names, known_ids, test_image, marked_attendance, attendance_file):
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.5)

        name = "Unknown"
        emp_id = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]
            emp_id = known_ids[first_match_index]

            mark_attendance(name, emp_id, marked_attendance, attendance_file)

        cv2.rectangle(test_image, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(test_image, f"{name} ({emp_id})", (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    return test_image

def mark_attendance(name, emp_id, marked_attendance, attendance_file):
    if name != "Unknown" and emp_id != "Unknown" and (name, emp_id) not in marked_attendance:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attendance_data = [name, emp_id, current_time]

        with open(attendance_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(attendance_data)

        marked_attendance.add((name, emp_id))

        print(f"Attendance marked for {name} (ID: {emp_id}) at {current_time}")
