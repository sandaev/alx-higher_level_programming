#!/usr/bin/python3
"""DEFINES A CLASS THAT INHERITS FROM list
    
    METHODS:
    --------
    print_sorted() - prints a sorted list
"""


class MyList(list):
    """ This class implements a method that print sorted list """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints sorted list"""
        lst = [i for i in self]
        lst.sort()
        print(lst)
