#!/usr/bin/python3
'''fuction to print string in uppercase'''


def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            s = chr(ord(s) - 32)
        else:
            s = s
        print("{:c}".format(s), end="")
    print("")
