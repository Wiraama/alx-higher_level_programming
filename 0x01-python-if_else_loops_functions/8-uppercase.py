#!/usr/bin/python3
'''fuction to print string in uppercase'''


def uppercase(str):
    for s in str:
        if 'a' <= s <= 'z':
            S = chr(ord(s) - 32)
        else:
            S = s
        print("{:c}".format(S), end="")
    print("")
