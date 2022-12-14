#!/usr/bin/python3
"""Function that prints name

say_my_name(first_name, last_name="") - Prints <first_name> <last_name>

Parameters:
    first_name (str)
    last_name(str)
"""


def say_my_name(first_name, last_name=""):
    "Prints <first_name> <last_name>"
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if first_name is None:
        raise TypeError("say_my_name() missing 1 required positional argument: 'first_name'")

    print("{} {}".format(first_name, last_name))
