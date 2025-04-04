import subprocess
import os

class DirectoryOpener:
    def __init__(self, directory_path):
        self.directory_path = "./known_faces"

    def open_directory_in_file_explorer(self):
        try:
           
            self.directory_path = os.path.normpath(self.directory_path)

          
            if os.name == 'nt': 
                subprocess.Popen(['explorer', self.directory_path], shell=True)
            
            else:
                print("Unsupported operating system. Unable to open the directory in a file explorer.")

        except FileNotFoundError:
            print(f"The directory '{self.directory_path}' does not exist.")
        except PermissionError:
            print(f"You do not have permission to access the directory '{self.directory_path}'.")

if __name__ == "__main__":
    directory_path = "./known_faces"
    opener = DirectoryOpener(directory_path)
    opener.open_directory_in_file_explorer()
