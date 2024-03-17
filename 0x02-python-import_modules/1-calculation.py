#!/usr/bin/python3
'''program that import function frm the file , does some math and print results'''

if __name__ == "__main__":
    from calculator_1 import sub, add, mul, div
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
