#!/usr/bin/python3
"""Defines a function that prints a square

print_square(size): Prints a square with '#'
    Parameter:
        size (int): size of square
"""


def print_square(size):
    """Prints a square with '#'"""

    if type(size) not in [int, float] or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size > 100:
        raise ValueError("size too large")

    size = int(size)

    for row in range(size):
        print("{}".format('#' * size))
