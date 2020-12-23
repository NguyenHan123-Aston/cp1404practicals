"""
CP1404 7th Practical
Coding to check password
Nguyen Hoang Ba Han - 13587248
"""

# Using constants in ALL_CAPS
# a. minimum and maximum length of the password
PASS_MIN_LENGTH = 5
PASS_MAX_LENGTH = 15
SPECIAL_CHAR_REQUIRED = False
SPECIAL_CHAR_NOT_REQUIRED = "!@#$%^&*()_-=+`~,./'[]<>?{}| "


def main():
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(PASS_MIN_LENGTH, PASS_MAX_LENGTH))
    print("\t 1 or more uppercase characters")
    print("\t 1 or more lowercase characters")
    print("\t 1 or more numbers")
    if SPECIAL_CHAR_REQUIRED:
        print("\t and 1 or more special characters:  ", SPECIAL_CHAR_NOT_REQUIRED)
    password = input(">")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(
        len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    if len(password) < PASS_MIN_LENGTH or len(password) > PASS_MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in SPECIAL_CHAR_NOT_REQUIRED:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if SPECIAL_CHAR_REQUIRED:
        if count_special == 0:
            return False

    return True


main()
