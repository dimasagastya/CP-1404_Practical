

def get_number(lower, upper):
    while True:
        try:
            number = int(input("Enter a number ({}-{}):\n >>>".format(lower,upper)))
            if number < lower or number > upper:
                print("Please enter a valid number!")
            else:
                return number
        except ValueError:
            print("Please enter a valid number!")

return_value = get_number(10,50)
print("The returned value is {}".format(chr(return_value)))