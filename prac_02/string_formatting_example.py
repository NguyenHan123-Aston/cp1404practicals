"""
CP1404 1st Practical
Pseudo code for using string formatting
Nguyen Hoang Ba Han - 13587248
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035

# Print the sentence using formatting
print("{} {} for about ${:,.2f}".format(year, name, cost))

# Aligning columns:
numbers = [0, 50, 100, 150]
for i, number in enumerate(numbers):
    print("{1:>4}".format(i + 1, number))

