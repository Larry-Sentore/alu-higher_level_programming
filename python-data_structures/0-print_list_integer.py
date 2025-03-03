#!/usr/bin/python3
def print_list(my_list=[]):
    for i in my_list:
        print("{i}".format(i))

lol = [1,2,3,4,5]
print(print_list(lol))
