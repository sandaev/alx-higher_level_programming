#!/usr/bin/python3
""" FUNCTION THAT READS A TEXT FILE AND PRINTS THE 
    CONTENT TO STDOUT
"""


def read_file(filename=""):
    """ Reads a file and prints to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            print(line, end="")
