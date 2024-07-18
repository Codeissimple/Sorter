import os
import shutil

# define the path to the target folder
target_folder = os.path.expanduser("~/Downloads")
# list all files in the target folder
folders = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Audios': ['.mp3', '.wav']
    'Archives': ['.zip', '.bz2', '.tar.gz', '.xz', '.rar', '.gz', '.bz2', '.tar.gz'],
    'Installers': ['.exe', '.bat', '.batc'],
    'Books': ['.epub', '.epubx', '.pptx'],
    'Excel': ['.xls', '.xlsx', '.ppt'],
    'HTML': ['.html', '.htm'],
}

# function to create folders if they don't exist

def create_folder(base_path, folder_names):
    for folder in folder_names:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Move files to their respective folders
def move_files(base_path, files, folder_dict):
    for file in files:
        file_path = os.path.join(base_path, file)
            if os.path.isfile(file_path):














