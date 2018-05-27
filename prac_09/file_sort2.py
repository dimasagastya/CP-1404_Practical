import os, shutil

os.chdir('file_sort2')

sort_methods = {}
extensions = []

# getting file extensions
for name in os.listdir('.'):
    if not os.path.isdir(name):
        ext = name.split('.')[1]
        if not ext in extensions: extensions.append(ext)

# get user option for sorting method
for ext in extensions:
    option = input("What category would you like to sort {} files into? ".format(ext))
    if option in sort_methods.keys():
        sort_methods[option] += ext + " "
    else:
        sort_methods[option] = ext + " "

# creating folders in user favored name
for ext in sort_methods.keys():
    if not os.path.exists(ext): os.mkdir(ext)


for name in os.listdir('.'):
    if not os.path.isdir(name):
        for key, value in sort_methods.items():
            if name.split('.')[1] in value:
                shutil.move(name, key)

