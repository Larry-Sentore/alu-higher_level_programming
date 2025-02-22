#!/usr/bin/python3
def uppercase(line):
    for word in line:
        if 97 <= ord(word) <== 122:
            word = chr(ord(word) - 32)
        print("{}".format(word), end="")
    
