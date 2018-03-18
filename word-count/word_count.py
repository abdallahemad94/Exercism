import re


def word_count(phrase):
    clean_phrase = re.sub('[^0-9a-zA-Z\']+', ' ', phrase)
    pattern = re.compile('(\w+\'?\w+|\d+)')
    words = pattern.findall(clean_phrase)
    counter = {}
    for word in words:
        counter[word.lower()] = counter.get(word.lower(), 0) + 1
    return counter
