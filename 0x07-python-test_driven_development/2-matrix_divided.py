#!/usr/bin/python3
"""Fucntion that divides matrix by an integer

matrix_divided(matrix, div) -> list:
    matrix(list)
    div(int)
"""


def matrix_divided(matrix, div):
    """Divides matrix by div, returns a new matrix"""
    row_len = len(matrix[0])

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[i]) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(matrix[row][col] / div, 2) for col in
            range(len(matrix[row]))] for row in range(len(matrix))]
