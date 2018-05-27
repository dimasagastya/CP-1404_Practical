
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError happen?
-> A ValueError happens when the values that the user put inside the numerator or denominator are not match with the data type.
2. When will a ZeroDivisionError happen?
-> A ZeroDivisionError will occur when the user put the '0' number inside the denominator.
3. Can you change the code to evade the possibility of a ZeroDivisionError?
-> Yes, we can use loop code to keep asking the user to put different value until it is not a '0' value.
"""
