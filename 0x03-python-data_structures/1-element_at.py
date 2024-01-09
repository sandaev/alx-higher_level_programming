#!/usr/bin/python3
"""Function retrieves an element from a list

    my_list: List to work on
    idx: index of element

    Return: element on success; None otherwise
"""


def element_at(my_list, idx):

    if idx < 0 or idx >= len(my_list):
        return (None)
    else:
        return (my_list[idx])
