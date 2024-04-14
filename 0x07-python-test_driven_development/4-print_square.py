#!/usr/bin/python3

def print_square(size):
    """function that prints a square with the character #."""

    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for num in range(size):
            print("#" * size)
