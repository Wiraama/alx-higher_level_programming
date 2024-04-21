#!/usr/bin/python3
""" module to inherit rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square """

    def __init__(self, size):
        """
            fuction to instatiate with size

            args:
                size - private, positive integer showing length of class
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
            returns area of sqquare
        """
        return self.__size ** 2
