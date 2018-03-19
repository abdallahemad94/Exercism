def decode(string):
    digit = ''
    letter = ''
    decoded = ''
    for i in string:
        if i.isdigit():
            digit += i
        else:
            letter += i
            if digit:
                decoded += int(digit) * letter
            else:
                decoded += letter
            letter = ''
            digit = ''
    return decoded


def encode(string):
    encoded = ''
    count = 0
    for i in range(len(string)):
        if string[i] == encoded[-1:]:
            continue
        for j in string[i:]:
            if string[i] == j:
                count += 1
            else:
                break
        if count > 1:
            encoded += str(count) + string[i]
            count = 0
        else:
            encoded += string[i]
            count = 0
    return encoded
