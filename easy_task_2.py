import os

list_dir = os.listdir()
dir_find = [i for i in list_dir if os.path.isdir(i)]
print(list_dir)
