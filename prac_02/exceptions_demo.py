"""
CP1404 4th Practical
Example code using exception
Nguyen Hoang Ba Han - 13587248
"""
"""
1. When will a ValueError occur?
 - A ValueError occur when the numerator and/or denominator is in word form.
2. When will a ZeroDivisionError occur?
- A ZeroDivisionError occur when the denominator input is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Print "Denominator can't be 0" to get more notice and apply code "while... == 0" reduce the possibility of a ZeroDivisionError
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (Denominator can't be 0): "))
    while denominator == 0:
        print("Please input again")
        denominator = int(input("Enter the denominator (Denominator can't be 0): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
