import cv2
import os
import time
import tkinter as tk
from tkinter import simpledialog, messagebox
import shutil

def capture_and_save_images(emp_name, emp_id, num_images_to_capture=100):
    """
    Captures images from the webcam and saves them in a folder named 'name_empid'.

    :param emp_name: Employee name to be included in the folder and file names.
    :param emp_id: Employee ID to create a unique folder and file names.
    :param num_images_to_capture: Number of images to capture.
    """
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    # Create the 'images' directory if it doesn't exist
    images_dir = os.path.join(os.getcwd(), 'images')
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # Create a unique folder name using emp_name and emp_id
    folder_name = f"{emp_name}_{emp_id}"
    unique_folder_path = os.path.join(images_dir, folder_name)
    if not os.path.exists(unique_folder_path):
        os.makedirs(unique_folder_path)

    image_number = 1
    while image_number <= num_images_to_capture:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if not ret:
            print("Error capturing frame. Exiting...")
            break

        # Display the resulting frame
        cv2.imshow('Capture Image', frame)

        # Save the captured image with the name in the path
        image_path = os.path.join(unique_folder_path, f'{emp_name}_{emp_id}_{image_number}.jpg')
        cv2.imwrite(image_path, frame)
        print(f'Image {image_number} saved: {image_path}')

        image_number += 1
        time.sleep(0.2)

        # Check if the user pressed the 'q' key to quit early
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def get_emp_details_from_user():
    """
    Prompts the user to enter their name and employee ID through a Tkinter dialog.

    :return: A tuple containing the employee name and ID entered by the user.
    """
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to enter their name
    emp_name = simpledialog.askstring("Input", "Enter Your Name:", parent=root)
    
    # Prompt the user to enter their employee ID
    emp_id = simpledialog.askstring("Input", "Enter Employee ID:", parent=root)
    
    # Destroy the Tkinter root window
    root.destroy()

    return emp_name, emp_id

def show_error_message(message):
    """
    Shows an error message in a Tkinter message box.

    :param message: The error message to display.
    """
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()

    # Show the error message
    messagebox.showerror("Error", message)
    
    # Destroy the Tkinter root window
    root.destroy()

def manage_employee_folder(emp_name, emp_id):
    """
    Checks if the folder for the given employee ID exists and either deletes it or shows 'ID not found' in a Tkinter message box.

    :param emp_name: Employee name to be included in the folder name.
    :param emp_id: Employee ID to be included in the folder name.
    :return: True if the folder was successfully managed, False otherwise.
    """
    images_dir = os.path.join(os.getcwd(), 'images')
    folder_name = f"{emp_name}_{emp_id}"
    unique_folder_path = os.path.join(images_dir, folder_name)

    if os.path.exists(unique_folder_path):
        # Remove the existing folder and its contents
        shutil.rmtree(unique_folder_path)
        print(f"Existing folder for '{folder_name}' deleted.")
        return True
    else:
        show_error_message(f"Employee '{folder_name}' not found.")
        return False

def main():
    emp_name, emp_id = get_emp_details_from_user()
    if emp_name and emp_id:
        if manage_employee_folder(emp_name, emp_id):
            capture_and_save_images(emp_name, emp_id)
        else:
            print("Failed to manage folder. Exiting...")
    else:
        print("No name or employee ID entered. Exiting...")

if __name__ == "__main__":
    main()
