"""
CP1404 3rd practical
Pseudo code for sales calculate
Nguyen Hoang Ba Han - 13587248
"""
"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""

SALE = (float(input("Enter price: $")))
print(SALE)
# Calculate percent sale by using if else
if SALE > 1000:
    discount_bonus = SALE * 0.15
else:
    discount_bonus = SALE * 0.1
print("Your bonus sale is $", discount_bonus, sep=' ')

"""Now add a loop to ask repeatly until code input negative number"""
SALE = (float(input("Enter price: $")))
print(SALE)
while SALE >= 0:
    # Calculate percent sale by using if else
        if SALE > 1000:
            discount_bonus = SALE * 0.15
        else:
            discount_bonus = SALE * 0.1
        print("Your bonus sale is $", discount_bonus, sep = '')
        SALE = float(input("Enter price: $"))
