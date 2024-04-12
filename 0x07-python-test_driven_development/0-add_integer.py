#!/bin/python3
"""
    rototype: def add_integer(a, b=98):
    a and b must be integers or floats,
    otherwise raise a TypeError exception with the message a must be an 
    integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    You are not allowed to import any module
"""

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
