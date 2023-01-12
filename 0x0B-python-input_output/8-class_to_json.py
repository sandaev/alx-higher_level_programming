#!/usr/bin/python3
""" DEFINES A FUNCTION THAT RETURNS DICTIONARY DISCRIPTION WITH SIMPLE
    DATA STRUCTURE FOR JSON SERIALIZATION
"""


def class_to_json(obj):
    """ Returns dictionary description of object for json
        serialization
    """

    return (obj.__dict__)
