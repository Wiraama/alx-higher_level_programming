#!/usr/bin/python3
""" modulo """


class BaseGeometry:
    """ class BaseGeometry (based on 6-base_geometry.py) """

    def area(self):
        """public innstance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """functin to validate vale"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
        else:
            self.name = name
            self.value = value
