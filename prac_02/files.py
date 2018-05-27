#Exercise 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

#Exercise 2
inside_file = open("name.txt", "r")
name = inside_file.read().strip()
print("Your name is", name)
inside_file.close()

#Exercise 3
open_file = open("numbers.txt", "r")
number1 = int(open_file.readline())
number2 = int(open_file.readline())
print(number1 + number2)
open_file.close()

#Exercises 4
from_file = open("numbers.txt", "r")
total = 0
for line in from_file:
 number = int(line)
total += number
print(total)
from_file.close()

