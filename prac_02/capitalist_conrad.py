"""
CP1404 3rd Practical
Code to estimate stock-price simulator for a volatile stock
Nguyen Hoang Ba Han - 13587248
"""

import random

# Naming the increase and decrease limit

input_price = 10.0
price_increase_percent = 0.1
# 10%
price_decrease_percent = 0.05
# 5%
price_highest_limit = 1000.0
price_lowest_limit = 0.01
OUTPUT_FILE = "stock.txt"

out_file = open(OUTPUT_FILE, 'w')

price = input_price
date = 0
print("Starting price:  ${:.2f}".format(price), file=out_file)

while price >= price_lowest_limit and price <= price_highest_limit:
    price_change = 0
    date += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, price_highest_limit)
    else:
        price_change = random.uniform(- price_lowest_limit, 0)

    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(date, price), file=out_file)

out_file.close()
