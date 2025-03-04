#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = set()
    for word in set_2:
        if word in set_1:
            common.add(word)
    return common
