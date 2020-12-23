"""
CP1404 4th Practical
Coding loops to display odd numbers
Nguyen Hoang Ba Han - 13587248
"""
""" Displaying odd numbers from 1 to 20"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

""" Displaying 10s from 1 to 100"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()

""" Displaying reduce 1 from 20 to 1"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""Display the * as much as n (number) input"""
n = (int(input("Number of stars: ")))
for i in range(n):
    print("*", end=' ')
print()

"""Display the number of star increasing to the input number"""
for i in range(1, n + 1):
    print("*" * i)
print()
