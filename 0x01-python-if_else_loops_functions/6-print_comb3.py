#!/usr/bin/python3
'''prints all possible different combinations of two digits.'''
for num in range(10):
    for number in range(num + 1, 10):
        if num == 8 and number == 9:
            print("{}{}".format(num, number))
        else:
            print("{}{}".format(num, number), end=", ")
