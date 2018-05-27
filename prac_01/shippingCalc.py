__author__ = 'Hansel Tertius'
"""
The program allows the user to enter the number of items and the shipping cost for each different item.
Then the program computes and displays the total shipping cost.
If the total shipping cost is over $100, then a 10% discount is applied to the total shipping cost before the amount is displayed on the screen.
"""
item = int(input("Enter the number of item: "))
while item < 0:
    print("Invalid number of items!")
    item = int(input("Enter the number of item: "))
price = float(input("Enter the price for each item: $ "))
cost = item * price
if cost > 100:
    cost = cost - (0.1 * cost)
else:
    cost = cost
print("The cost is $ {:.2f}".format(cost))