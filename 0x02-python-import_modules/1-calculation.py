#!/usr/bin/python3
'''program that import function frm the file , does some math and print results'''


from calculator_1 import sub, add, mul, div
a = 10
b = 5
print(f"{a:d} - {b:d} = {sub(a, b)}")
print(f"{a:d} + {b:d} = {add(a, b)}")
print(f"{a:d} * {b:d} = {mul(a, b)}i")
print(f"{a:d} / {b:d} = {div(a, b)}")
