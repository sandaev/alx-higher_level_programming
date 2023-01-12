#!/usr/bin/python3
""" FUNCTION THAT WRITES AN OBJECT TO A TEXT
    FILE, USING JSON REPRESENTATION
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file, using json rep """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
