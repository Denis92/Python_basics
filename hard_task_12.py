import os
import shutil

dir_path = os.path.sep.join(input("Input path to dir: ").split(" ")) + os.path.sep
files = os.listdir(dir_path)
list_dir = [dir_path + i for i in files if ((os.path.isdir(dir_path + i)) and ("." in i))]
for i in list_dir:
    list_files = os.listdir(i + os.path.sep)
    for j in list_files:
        shutil.move(i + os.path.sep + j, dir_path)
for i in list_dir:
    os.rmdir(i)
