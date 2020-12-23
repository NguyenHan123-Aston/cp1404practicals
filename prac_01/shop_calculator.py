"""
CP1404 5th Practical
Code to work out the total price for a number of items
Nguyen Hoang Ba Han - 13587248
"""
total = 0
number_of_items = (int(input("Number of items: ")))
# Using while coding to ensure the input will not be negative
while number_of_items < 0:
        print("Invalid input! Please try again")
        number_of_items = (int(input("Number of items: ")))

# Since items input is postive, total price of item will be input equal to amount of items
for i in range(number_of_items):
    price_of_item = (float(input("Price of item: $")))
    total += price_of_item

# If the total price of item is more than $100, customer will receive 10% discount
if total > 100:
    total *= 0.9
    print("You have a discount of 10%")
print("Total price for {} item is $ {:.2f}".format(number_of_items, total))

