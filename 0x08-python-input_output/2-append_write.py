#!/usr/bin/python3
""" THIS FUNCTION APPENDS A STRING AT THE END OF A TEXT FILE
    AND RETURNS THE NUMBER OF CHARACTERS ADDED
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as f:
        num_char = f.write(text)
    return (num_char)
