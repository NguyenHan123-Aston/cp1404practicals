"""
CP1404 5th Practical
Code a program that gets integer
Nguyen Hoang Ba han - 13587248
"""

finished = False
result = 0
while not finished:
    try:
        result = (int(input("Please enter an integer: ")))
        finished = True

    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
