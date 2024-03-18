#!/usr/bin/python3
"""mports all functions from the file calculator_1.py
and handles basic operations."""


if __name__ == "__main__":
    import sys

    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    operator = sys.argv[2]
    num2 = int(sys.argv[3])

    if operator == "+":
        print("{} {} {} = {}".format(num1, operator, num2, add(num1, num2)))
    elif operator == "-":
        print("{} {} {} = {}".format(num1, operator, num2, sub(num1, num2)))
    elif operator == "*":
        print("{} {} {} = {}".format(num1, operator, num2, mul(num1, num2)))
    elif operator == "/":
        print("{} {} {} = {}".format(num1, operator, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
