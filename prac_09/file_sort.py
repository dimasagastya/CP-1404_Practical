
import os, shutil
os.chdir('file_sort')
for name in os.listdir('.'):
    if not os.path.isdir(name):
        ext = name.split('.')[1]
        if not os.path.exists(ext): os.mkdir(ext)
        shutil.move(name, ext)