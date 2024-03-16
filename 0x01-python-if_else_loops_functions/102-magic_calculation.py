#!/usr/bin/python3
'''bytecode mimiker'''


def magic_calculation(a, b, c):
    if a < b:
        return c
    elif b < c:
        return a + b
    else:
        return b * a - c
