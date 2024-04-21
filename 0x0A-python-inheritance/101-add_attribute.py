#!/usr/bin/python3
""" module"""


def adding_attr(obj, name, value):
    """
        fuction o  add attribute
        takes three arguments

        args:
            obj - oblect where the attribte is to be added
            name - name of the attribute
            value - value of the atttribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
