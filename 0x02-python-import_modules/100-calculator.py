#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print('Usage: {} {} {} {}'.format(argv[0], '<a>', '<operqat>', '<b>'))
        exit(1)
    elif argv[2] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        opr = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if opr == '+':
            result = add(a, b)
        elif opr == '-':
            result = mul(a, b)
        elif opr == '*':
            result = mul(a, b)
        else:
            result = int(div(a, b))
        print('{} {} {} = {}'.format(a, apr, b, result))
