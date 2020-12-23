"""
CP1404 3rd practical
Pseudo code for score calculating
Nguyen Hoang Ba Han - 13587248
"""
SCORE = (float(input("Enter score: ")))
print(SCORE)
# Using if-else format to find the result for each score input

if SCORE < 0 or SCORE > 100:
    print("Invalid score. Please try again")
else:
    if SCORE >= 90:
        print("Excellent")
    elif SCORE >= 80:
        print("Great")
    elif SCORE >= 50:
        print("Passable")
    elif SCORE < 50:
        print("Bad")
    else:
        print("Invalid score. Please try again")
print("Thank you")
