import os

dirs_files = os.listdir("files")  # корневая папка
print(dirs_files)  # список директорий и файлов
files_dirs = []
for d in dirs_files:
    if "." not in d:
        files_dirs.append(d)
    else:
        files_dirs.insert(0, d)
print(files_dirs)  # список файлов и директорий
