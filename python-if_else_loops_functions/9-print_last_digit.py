#!/usr/bin/python3
def last_digit(num):
    last = abs(num) % 10
    last = ord(str(last))
    return last
