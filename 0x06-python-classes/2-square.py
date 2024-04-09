#!/usr/bin/python3

"""class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """class defination"""
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError as e:
            print (e)
        except ValueError as e:
            print (e)
