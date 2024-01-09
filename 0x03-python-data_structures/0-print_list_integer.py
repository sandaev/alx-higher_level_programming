#!/usr/bin/python3
"""This function prints integers from list passed to it

    my_list: List to print from

    Return: Nothing
"""


def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
