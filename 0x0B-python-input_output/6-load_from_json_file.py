#!/usr/bin/python3
""" DEFINES A FUNCTION THAT CREATES AN OBJECT FROM A JSON FILE """


import json

def load_from_json_file(filename):
    """ Creates an object from a JSON """
    with open(filename, 'r') as f:
        for line in f.readlines():
            print(json.loads(line))
