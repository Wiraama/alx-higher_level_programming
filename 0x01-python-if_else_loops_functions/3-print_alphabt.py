#!/usr/bin/python3
'''prints the ASCII alphabet, in lowercase, not followed by a new line except q and e'''
for letter in range(97, 123):
    if chr(letter) in ['q', 'e']:
        continue
    print("{:c}".format(letter), end="")
