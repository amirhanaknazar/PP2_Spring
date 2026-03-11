#FILE HANDLING
#write_files.py

file = open("sample.txt", "w")

file.write("Hello world\n")
file.write("This is a file handling example\n")

file.close()

#read_files.py

file = open("sample.txt", "r")

content = file.read()
print(content)

file.close()

#Append lines

file = open("sample.txt", "a")

file.write("New line added\n")

file.close()

#copy_delete_files.py

import shutil
import os

# copy file
shutil.copy("sample.txt", "backup.txt")

# delete file safely
if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("File deleted")
else:
    print("File not found")