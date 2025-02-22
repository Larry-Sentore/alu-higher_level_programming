#!/usr/bin/python3
def uppercase(line):
    words = line.split()
    for word in words:
        for char in word:
            if 97 <= ord(word) <== 122:
                word = chr(ord(word) - 32)
            print("{}".format(word), end="")
        print(" ", end="")
    
