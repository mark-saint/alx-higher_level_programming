#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = args[1]
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    else:
        a = int(args[0])
        b = int(args[2])

        if operator == '+':
            func = add
        elif operator == '-':
            func = sub
        elif operator == '*':
            func = mul
        elif operator == '/':
            func = div
        print("{} {} {} = {}".format(a, operator, b, func(a, b)))
