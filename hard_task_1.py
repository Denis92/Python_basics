import os

dir_path = os.path.sep.join(input("Input path to dir: ").split(" ")) + os.path.sep
print(dir_path)
files = os.listdir(dir_path)
exts = [os.path.splitext(i)[1] for i in files if "." in i]
for i in set(exts):
    if not os.path.exists(os.path.join(dir_path, i)):
        os.mkdir(os.path.join(dir_path, i))

for file in files:
    destination = os.path.splitext(file)[1]
    os.rename(os.path.join(dir_path, file), os.path.join(dir_path, destination, file))
