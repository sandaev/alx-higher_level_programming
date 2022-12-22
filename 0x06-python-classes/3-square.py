#!/usr/bin/python3
'''Conatins a class the defines a square'''


class Square:
    '''This class defines a square with size and method
    that calculates the area

    Attributes:
    __size(int) - Lenght of side which must be integer
    and greater than or equal to 0

    area() - Public instance method that returns the area of square
    '''

    def __init__(self, __size=0):
        '''Constructor for the instances

        Attributes:

        _Square__size(int) - length of the square
        '''

        try:
            if isinstance(__size, str):
                raise TypeError
            if __size < 0:
                raise ValueError
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
        else:
            self._Square__size = __size

    def area(self):
        '''Calculates the area of sqaure object

        Return (int) - Area of sqaure
        '''

        return self._Square__size * self._Square__size
