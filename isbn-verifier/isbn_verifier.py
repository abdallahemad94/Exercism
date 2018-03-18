import re


def verify10(isbn: str) -> bool:
    """
    Takes an ISBN number as a string and check if it is a valid ISBN-10.
    :param isbn: ISBN number as string.
    :return: True if valid and False if not.
    """
    total = 0
    isbn10 = re.compile('^(\d)\W?(\d{3})\W?(\d{5})\W?([\dXx])$')
    if re.match(isbn10, isbn):
        isbn = re.sub('\W*', '', isbn)
        length = len(isbn)
        for i in range(length):
            if isbn[i].isdigit():
                total += int(isbn[i]) * (length - i)
            elif isbn[i].lower() == 'x':
                total += 10 * (length - i)
        return total % 11 == 0
    return False


def verify13(isbn: str) -> bool:
    """
    Takes an ISBN number as a string and check if it is a valid ISBN-13.
    :param isbn: ISBN number as a string.
    :return: True if valid and False if not.
    """
    total = 0
    isbn13 = re.compile('^(\d{3})\W*(\d)\W*(\d{3})\W*(\d{5})\W*(\d)$')
    if re.match(isbn13, isbn):
        isbn = re.sub('\W*', '', isbn)
        for index, digit in enumerate(isbn):
            if index % 2 != 0:
                total += int(digit) * 3
            else:
                total += int(digit)
        return total % 10 == 0
    return False


def gen13(isbn10: str) -> str:
    """
    Takes an ISBN-10 number and generate a valid ISBN-13 from it.
    :param isbn10: ISBN-10 number as a string.
    :return: a string containing the generated ISBN-13 number.
    """
    if verify10(isbn10):
        isbn13 = '978-' + isbn10[0:-1]
        isbn13_copy = re.sub('\W*', '', isbn13)
        total = 0
        for index, digit in enumerate(isbn13_copy):
            if index % 2 != 0:
                total += int(digit) * 3
            else:
                total += int(digit)
        isbn13 += str(10 - (total % 10))
        if verify13(isbn13):
            return isbn13
    return "{} is an invalid ISBN-10 number".format(isbn10)
