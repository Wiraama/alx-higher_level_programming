#!/usr/bin/python3
"""unction that returns the list of
available attributes and methods of an object"""


def lookup(obj):
    """return list of attr and meth"""

    return dir(obj)
