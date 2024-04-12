#!/bin/python3

def add_integer(a, b=98):
    """unction that adds 2 integers."""


    if type(a) is not int and type(a) is not float:
        """you can use if not isinstance(a, (int, float)):
        works perfect"""

        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
