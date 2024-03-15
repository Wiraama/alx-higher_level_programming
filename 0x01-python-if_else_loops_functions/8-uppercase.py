#!/usr/binn/python3
'''fuction to print string in uppercase'''


def uppercase(str):
    for s in str:
        if 'a' <= s <= 'z':
            '''mean is a lowercase cahracter'''
            uppers = chr(ord(s) - 32)
        else:
            uppers = s
        print(uppers, end="")
