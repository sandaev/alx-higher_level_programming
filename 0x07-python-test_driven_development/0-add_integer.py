#!/usr/bin/python3
"""Function that returns sum of two integers

add_integer(a, b=98) -> int:
    a (int) - Mandatory argument
    b=98 (int) - Optional arguemnt
"""


def add_integer(a, b=98):
    """Returns the sum of a and b"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if a is None:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
