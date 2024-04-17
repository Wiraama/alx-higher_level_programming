#!/usr/bin/python3
"""unction that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Printing content in a file"""
    with open(filename, mode='r', encoding=("utf-8")) as f:
        myfile = f.read()
        print(myfile, end="")
