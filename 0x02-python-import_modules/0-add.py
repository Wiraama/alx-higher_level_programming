#!/usr/bin/python3
'''mports the function def add(a, b): from the file add_0.py and prints the result of the addition'''


a = 1
b = 2
from add_0 import add
c = add(a, b)
print("{} + {} = {}".format(a, b, c))
