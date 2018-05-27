"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""

    if len (password) > 6:
        print("This password is too long. Make is shorter.")
    elif len (password) < 2:
        print("This password is too short. Make it longer.")
    else:
        print("This password is good.")

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for i in password:

        if i.islower():
            count_upper += 1
        elif i.isupper():
            count_lower += 1
        elif i.isdigit():
            count_digit += 1
        else:
            count_special += 1

    if count_upper == 0 or count_lower == 0 or count_digit == 0:
        return False
    else:return True

    if count_special == 0:
        return False
    else: return True

main()