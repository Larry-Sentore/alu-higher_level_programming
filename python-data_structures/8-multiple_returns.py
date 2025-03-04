#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    length = len(sentence)
    for char in sentence:
        first = char
        break
    output = (length, first)
    return output
