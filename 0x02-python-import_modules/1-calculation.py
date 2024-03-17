#!/usr/bin/python3
'''program that import function frm the file , does some math and print results'''

if __name__ == "__main__":
    from calculator_1 import sub, add, mul, div
    a = 10
    b = 5
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}i")
    print(f"{a} / {b} = {div(a, b)}")
