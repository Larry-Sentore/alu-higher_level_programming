#!/usr/bin/python3
def islower(c):
    if 97 <= ord(c) <= 122:
        print("{} is lower".format(c))
    else:
        print("{} is upper".format(c))
