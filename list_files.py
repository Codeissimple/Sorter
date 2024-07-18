import os
import shutil

# define the path to the target folder
target_folder = os.path.expanduser("~/Downloads")
# list all files in the target folder
folders = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Audios': ['.mp3', '.wav'],
    'Archives': ['.zip', '.bz2', '.tar.gz', '.xz', '.rar', '.gz', '.bz2', '.tar.gz'],
    'Installers': ['.exe', '.bat', '.batc'],
    'Books': ['.epub', '.epubx', '.pptx'],
    'Excel': ['.xls', '.xlsx', '.ppt'],
    'HTML': ['.html', '.htm'],
}

# function to create folders if they don't exist

def create_folders(base_path, folder_names):
    for folder in folder_names:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Move files to their respective folders
def move_files(base_path, files, folder_dict):
    for file in files:
        file_path = os.path.join(base_path, file)
        if os.path.isfile(file_path):
            file_extention = os.path.splitext(file)[1].lower()
            moved = False
            for folder, extentions in folder_dict.items():
                if file_extention in extentions:
                    shutil.move(file_path, os.path.join(base_path, folder, file))
                    moved = True
                    break
            if not moved:
                print(f'No matching folder for file: {file}')
# Create folder
create_folders(target_folder, folders.keys())

files = os.listdir(target_folder)

# Move the files
move_files(target_folder, files, folders)

print("Files have beed sorted.")












