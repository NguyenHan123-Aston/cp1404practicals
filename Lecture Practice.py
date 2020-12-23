import string

def count_letters(text):
    """Count the number of letters in text"""
    count = 0
    for character in text:
        if character.lower() in string.ascii_letters:
            count += 1
    return count
