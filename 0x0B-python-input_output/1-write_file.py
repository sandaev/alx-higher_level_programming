#!/usr/bin/python3
""" FUNCTION THAT WRITES A STRING TO A TEXT FILE AND
    NUMBER OF CHARACTER WRITTEN
"""


def write_file(filename="", text=""):
    """  Writes a string to a text file """
    with open(filename, 'w', encoding="utf-8") as f:
        num_char = f.write(text)
    return (num_char)
