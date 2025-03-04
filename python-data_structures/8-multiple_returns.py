#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    length = len(sentence)
    for char in sentence:
        first = char
        break
    output = (length, first)
    return output
