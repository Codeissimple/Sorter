import os
# define the path to the target folder
target_folder = os.path.expanduser("~/Downloads")
# list all files in the target folder
files = os.listdir(target_folder)
# print the list of files
print(files)