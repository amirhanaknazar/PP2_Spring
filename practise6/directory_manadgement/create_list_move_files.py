#os — Miscellaneous operating system interfaces

#This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module. For creating temporary files and directories see the tempfile module,
#and for high-level file and directory handling see the shutil module.

#os.chdir(path)
#Change the current working directory to path.

#This function can support specifying a file descriptor. 
#The descriptor must refer to an opened directory, not an open file.

#Example:
import os
os.chdir("test")

#os.getcwd()
#Return a string representing the current working directory.

import os
print(os.getcwd())


#os.listdir(path='.')
#Return a list containing the names of the entries in the directory given by path. 
#The list is in arbitrary order, and does not include the special entries '.' and
#'..' even if they are present in the directory. If a file 
#is removed from or added to the directory during the call of this function, 
#whether a name for that file be included is unspecified.

import os
files = os.listdir()
print(files)

#os.mkdir(path, mode=0o777, *, dir_fd=None)
#Create a directory named path with numeric mode mode.

#If the directory already exists, FileExistsError is raised. 
#If a parent directory in the path does not exist, FileNotFoundError is raised.
import os
os.mkdir("folder_name")

#os.makedirs(name, mode=0o777, exist_ok=False)
"""Recursive directory creation function. Like mkdir(), but makes all intermediate-level directories needed to contain the leaf directory.

The mode parameter is passed to mkdir() for creating the leaf directory; see the mkdir() description for how it is interpreted. To set the file permission bits of any newly created parent directories you can set the umask before invoking makedirs(). The file permission bits of existing parent directories are not changed.

If exist_ok is False (the default), a FileExistsError is raised if the target directory already exists.

Note makedirs() will become confused if the path elements to create include pardir (eg. “..” on UNIX systems).
This function handles UNC paths correctly."""

import os
os.makedirs("folder1/folder2/folder3")

#os.rmdir(path, *, dir_fd=None)
"""Remove (delete) the directory path. If the directory does not exist or is not empty,
a FileNotFoundError or an OSError is raised respectively. In order to remove whole directory trees, 
shutil.rmtree() can be used.

This function can support paths relative to directory descriptors."""

import os
os.rmdir("test")