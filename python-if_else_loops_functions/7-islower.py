#!/usr/bin/env python3
islower = __import__('7-islower').islower
def islower(c):
    if 97 <= ord(c) <= 122:
        print("{} is lower".format(c))
    else:
        print("{} is upper".format(c))
