#!/usr/bin/python3
'''alphabet in reverse order an in uppercase and lower case in a manner '''


for letter in range(ord('z'), ord('a') - 1, - 1):
    if letter % 2 == 0:
        print("{}".format(chr(letter)), end='')
    else:
        print("{}".format(chr(letter - 32)), end='')
