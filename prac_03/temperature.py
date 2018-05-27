"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def celciusConvert():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))

def farenheitConvert():
    farenheit = float(input("Farenheit: "))
    celsius = 5 / 9 * (farenheit - 32)
    print("Result: {:.2f} C".format(celsius))

def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celciusConvert()
        elif choice == "F":
            farenheitConvert()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()