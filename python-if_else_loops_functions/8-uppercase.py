#!/usr/bin/python3
def uppercase(str):
    for i, char in enumerate(str):
        if 97 <= ord(char) <= 122:  # Check if lowercase
            char = chr(ord(char) - 32)  # Convert to uppercase
        print("{}".format(char), end="")
    
