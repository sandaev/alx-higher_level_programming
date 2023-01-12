#!/usr/bin/python3
""" FUNCTION THAT RETURNS THE JSON REPRESENTATION OF AN
    OBJECT
"""
import json


def to_json_string(my_obj):
    """ Returns the json representation """
    return (json.dumps(my_obj))
