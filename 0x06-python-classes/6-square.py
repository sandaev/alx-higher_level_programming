#!/usr/bin/python3

'''Contains a class that defines a square, calculate area
Class
------
Square : defines a square

Methods
------
size ():
gets the size attribute

size(value): sets the size

area(): Calcualtes area of square

my_print(): Prints square

'''


class Square:
    '''This class defines a square with optional,
    private size with restrictions

    Atrributes:

    __size(int) - Length of side of square that must be greater than zero
    area - returns area
    my_print - prints sqaure
    '''

    def __init__(self, __size=0, __position=(0, 0)):
        '''Contsructor of the Sqaure class

        Attributes:

        _Square__size(int) - lenght of sqaure that must be greater
        than or eqaul to 0
        '''

        try:
            if isinstance(__size, str):
                raise TypeError
            if __size < 0:
                raise ValueError
        except TypeError:
            raise Exception("size must be an integer")
        except ValueError:
            raise Exception("size must be >= 0")
        else:
            self._Square__size = __size

        try:
            if isinstance(__position, tuple) or not \
                    isinstance(__position[0], int) or \
                    not isinstance(__position[1], int):
                raise TypeError
        except TypeError:
            raise Exception("positiom must be a tuple of 2 positive integers")
        else:
            self._Square__position = __position

    @property
    def size(self):
        '''Retrieves the valueof private attribute
        __size'''

        return self._Square__size

    @size.setter
    def size(self, value):
        '''Stes new value for __size attribute'''
        try:
            if isinstance(value, str):
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            raise Exception("size must be an integer")
        except ValueError:
            raise Exception("size must be >= 0")
        else:
            self._Square__size = value

    @property
    def property(self):
        '''getter for position property'''
        return self._Square__position

    @position.setter
    def property(self, value):
        '''setter for position property'''
        try:
            if not isinstance(value, tuple) or \
                    not isinstance(value[0], int) or \
                    not isinstance(value[1], int):
                raise TypeError
        except TypeError:
            raise Exception("position must be a tuple of 2 positive integers")
        else:
            self._Square__position = value

    def area(self):
        '''Returns the area of a Square object'''
        return self._Square__size * self._Square__size

    def my_print(self):
        '''prints to the stdout square with char #'''
        if self._Square__size == 0:
            print()
        else:
            for row in range(self._Square__size):
                print("{}{}".format(self._Square__position[0] * " ",
                      self._Square__size * "#"))
