#!/usr/bin/python3
"""function that creates an Object from a “JSON file”:"""


import json


def load_from_json_file(filename):
    """creating object from json"""

    with open(filename, 'w') as f:
        json.loads(f)
