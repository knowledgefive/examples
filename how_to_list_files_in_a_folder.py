# import the operating system
import os

# define a folder path
folder_path = "test"

# check to make sure the folder path exists
if not os.path.exists(folder_path):
    error_message = f"folder_path: {folder_path} not found"
    raise ValueError(error_message)

# list the files within the selected folder
files = os.listdir(folder_path)

# loop through the file names
for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    print(f"file_name: {file_name} in {file_path}")