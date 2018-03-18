def is_isogram(string):
    letters = set(string.lower())
    for letter in letters:
        if not letter.isalpha():
            continue
        if string.lower().count(letter) > 1:
            return False
    return True
