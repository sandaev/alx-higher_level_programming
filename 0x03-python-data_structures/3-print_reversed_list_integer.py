#!/usr/bin/python3
"""This function prints integers of a list in reversed order

    my_list: list to work on

    Return: Nothing
"""


def print_reversed_list_integer(my_list=[]):

    if len(my_list) == 0:
        print("{}".format(my_list))
    else:
        for i in range(-1, len(my_list) - 1, -1):
            print("{:d}".format(my_list[i]))
