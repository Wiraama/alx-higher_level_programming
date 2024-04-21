#!/usr/bin/python3
""" module to find area of a rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    class of rectangle
    """

    def __init__(self, width, height):
        """ fuctin to intatiate as in 8-rectangle.py """

        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

