"""
CP1404 2nd Practical
Pseudo code for random number
Nguyen Hoang Ba Han - 13587248
"""

import random
print(random.randint(5, 20))
# On line 1, the number change in integer
# On line 1, the smallest number is 5, the largest number is 20

print(random.randrange(3, 10, 2))
# On line 2, the output become odd number since it start with odd number
# Moreover, it set a limit range with 2, which become 3 - 5 - 7 - 9
# On line 2, the smallest number is 3, the largest number is 9

print(random. uniform(2.5, 5.5))
# On line 3, the output is in float form
# On line 3, the smallest number is 2.5, the largest number is 5.5

print(random.randint(1, 100))
