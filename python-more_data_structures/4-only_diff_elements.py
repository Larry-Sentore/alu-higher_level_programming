#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    different = set()
    for word in set_2:
        if word not in set_1:
            different.add(word)
    for letter in set_1:
        if letter not in set_2:
            different.add(letter)
    return different
