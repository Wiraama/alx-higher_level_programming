#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if number < 0:
    num = -num
    print(f"Last digit of {number:d} is {num:d} and is ", end="")
if num > 5:
    print(f"{number:d} and is greater than 5")
elif num == 0:
    print(f"{number:d} and is 0")
elif num < (6 and not 0):
    print(f"{number:d} and is less than 6 and not 0")
