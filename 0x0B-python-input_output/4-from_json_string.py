#!/usr/bin/python3
""" FUNCTION THAT CONVERTS JSON STRING TO OBJECT """
import json


def from_json_string(my_str):
    """ Converts json string to object """
    return json.loads(my_str)
