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

}