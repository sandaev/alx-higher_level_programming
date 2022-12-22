#!/usr/bin/python3
'''Contains a class that defines a square with constraints'''


class Square:
    '''This class defines a square with optional,
    private size with restrictions

    Atrributes:

    __size(int) - Length of side of square that must be greater than zero
    '''

    def __init(self, __size=0):
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
            else:
                self._Square__size = __size
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
