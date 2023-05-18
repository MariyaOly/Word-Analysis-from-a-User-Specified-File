def changeText(text):
    """
    Function that takes a string of text, removes all punctuation marks, and returns
    a list of words from the text.
    """
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(i, '')

    return text.split()


def mostCommon(text, length=0):
    """
    Function that takes a list and a length constraint, and returns the most commonly
    occurring element. If there are multiple elements with the same highest frequency,
    it will return all of them.
    """
    most_common = []
    qty_most_common = 0

    for item in text:
        if len(item) > length:
            qty = text.count(item)
            if qty > qty_most_common:
                qty_most_common = qty
                most_common = [item]
            elif qty == qty_most_common:
                most_common.append(item)

    return list(set(most_common))


def mostLength(text):
    """
    Function that takes a list and returns the longest element. If there are multiple
    elements with the same longest length, it will return all of them.
    """
    most_length = []
    qty_most_length = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for item in text:
        charEn = all(char in alphabet for char in item)

        if charEn:
            qty = len(item)
            if qty > qty_most_length:
                qty_most_length = qty
                most_length = [item]
            elif qty == qty_most_length:
                most_length.append(item)

    return list(set(most_length))


nameFile = input('File name: ')

with open(nameFile, encoding='utf8') as f:
    fileText = f.read()

fileText = changeText(fileText)
print(f'Most common words (length > 3): {mostCommon(fileText, 3)}')
print(f'Longest English words: {mostLength(fileText)}')
