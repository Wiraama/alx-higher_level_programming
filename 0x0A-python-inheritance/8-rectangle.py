#!/usr/bin/python3
"""module rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class recatangle inheriting from basegeometry class"""

    def __init__(self, width, height):
        """instatiate with width and height

        args:
            width: as positive int
            height: as positive int
        both sould be private
        """

        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
