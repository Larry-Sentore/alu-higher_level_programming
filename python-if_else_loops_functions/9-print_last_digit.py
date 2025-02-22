#!/usr/bin/python3
def print_last_digit(number):
    lastd = abs(number) % 10
    if number < 0:
        lastd = -lastd
    print(lastd, end="")
    return lastd
