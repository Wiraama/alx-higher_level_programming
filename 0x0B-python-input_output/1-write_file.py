#!/usr/bin/python3
"""function that writes a string to a text file
(UTF8) and returns the number of characters written:"""


def write_file(filename="", text=""):
    """writting to a file"""

    with open(filename, mode='w', encoding=("utf-8")) as f:
        my_file = f.write(text)
        return (my_file)
