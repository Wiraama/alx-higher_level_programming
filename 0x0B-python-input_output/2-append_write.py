#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:"""


def append_write(filename="", text=""):
    """appending text ta the end"""

    with open(filename, mode='a', encoding=("utf-8")) as f:
        fileme = f.write(text)
        return fileme
