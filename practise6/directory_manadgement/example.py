#DIRECTORY MANAGEMENT
#create_list_dirs.py

import os

# create nested directories
os.makedirs("test/folder1/folder2", exist_ok=True)

# list files and folders
files = os.listdir()

print(files)

#move_files.py

import shutil
import os

# create folders
os.makedirs("source", exist_ok=True)
os.makedirs("destination", exist_ok=True)

# move file
shutil.move("sample.txt", "destination/sample.txt")

# copy file
shutil.copy("destination/sample.txt", "source/sample_copy.txt")