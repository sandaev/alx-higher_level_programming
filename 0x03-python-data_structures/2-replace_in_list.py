#!/usr/bin/python3
"""Function that replaces and element at a specified index

    my_list: list to work on
    idx: index of element to replacement
    element: new element

    Return: new list on success, previous list otherwise
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        my_list[idx] = element
    return (my_list)
