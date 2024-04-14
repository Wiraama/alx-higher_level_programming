#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
