from string import ascii_lowercase


def is_pangram(sentence):
    for letter in ascii_lowercase:
        if sentence.lower().count(letter) > 0:
            continue
        return False
    return True
