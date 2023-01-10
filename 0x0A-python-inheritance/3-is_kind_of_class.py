#!/usr/bin/python3
"""RETURNS TRUE IF OBJECT IS AN ISTANCE OF OR
    OF THE CLASS THAT INHERITED FROM THE SPECIFIED CLASS
"""


def is_kind_of_class(obj, a_class):
    """ Checks if obj is an instance of a_class """
    return isinstance(obj, a_class)
