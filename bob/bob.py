import re


def hey(phrase):
    quest = r'^.*\?[\s]*$'
    yell = r'^[A-Z]+$'
    nothing = r'^[\s\W]*$'

    if re.match(quest, phrase):
        if re.match(yell, re.sub('[^a-zA-Z]*', '', phrase)):
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif re.match(yell, re.sub('[^a-zA-Z]*', '', phrase)):
        return "Whoa, chill out!"
    elif re.match(nothing, phrase):
        return 'Fine. Be that way!'
    return 'Whatever.'
