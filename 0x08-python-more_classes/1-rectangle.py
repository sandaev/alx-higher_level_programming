#!/usr/bin/python3
""" Defines a class for a Rectangle

Attributes:
    __width(int) - width of rectangle object
    __height(int) - height of rectangle object
"""


class Rectangle:
    """ Defines a rectangle with dimensions """
    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ GETS WIDTH """

        return self.__width

    @width.setter
    def width(self, value):
        """ SETS WIDTH """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ GETS HEIOGHT """

        return self.__height

    @height.setter
    def height(self, value):
        """ SETS HEIGHT """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
