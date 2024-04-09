#!/usr/bin/python3
"""class Square that defines a square by: (based on 3-square.py)"""


class Square:

    """class defination"""
    def __init__(self, size):
        """defines & initialize new attribute"""
        self.__size = size

    @property
    def size(self):

        """defines new method size"""
        return self.__size

    @size.setter
    def size(self, value):

        """defines metod and attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be n integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
