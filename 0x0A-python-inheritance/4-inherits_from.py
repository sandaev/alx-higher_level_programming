#!/usr/bin/python3
""" Checks for inheritance, directly or inderictly """


def inherits_from(obj, a_class):
    """ Tests inheritance of object and class"""
    return issubclass(type(obj), a_class)
