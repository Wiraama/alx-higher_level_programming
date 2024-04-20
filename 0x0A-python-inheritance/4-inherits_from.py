#!/usr/bin/python3
""" module to return if object is intancev"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False. """

    return type(obj) is not a_class and type(obj) != a_class
