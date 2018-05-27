"""
author = Hansel
"""
def main():
    name = get_name()
    for_loop(name)

def for_loop(name):
    for i in range(0,len(name),2):
        letter = name[i]
        print(letter,end=" ")

def get_name():
    name = input("Enter your name:")
    while len(name) == 0:
        print("Invalid name")
    return name


main()