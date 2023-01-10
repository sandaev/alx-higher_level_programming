#!/usr/bin/python3
"""Defines a function that checks if an object is of the
    sepcified type
"""


def is_same_class(obj, a_class):
    """ Returns True if obj is excatly of type a_class """
    if obj.__class__ == a_class:
        return True
    else:
        return False
