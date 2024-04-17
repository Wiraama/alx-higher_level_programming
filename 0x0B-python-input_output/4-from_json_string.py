#!/usr/bin/python3
""" function that returns an object (Python data structure)
represented by a JSON string:"""


import json


def from_json_string(my_str):
    """returns object represented by JSON string"""

    new_file = json.loads(my_str)
    return new_file
