#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if number < 0:
    num = -num
print(f"Last digit of {number:d} is {num:d} ", end="")
if num > 5:
    print("and is greater than 5")
elif num == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
