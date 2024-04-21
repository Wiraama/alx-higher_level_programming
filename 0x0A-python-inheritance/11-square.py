#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        class inheriting another class from  file 9
    """

    def __init__(self, size):
        """
            this fuction instatiate

            args:
                size - length of side of square
        """
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """
            discribes the square
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
            finds the area of the square
        """
        return self.__size ** 2
