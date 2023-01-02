#!/usr/bin/python3
"""Multiplies two matricces

matrix_mul(m_a, m_b):
    multiplies m_a and m_b if they can be multiplied
Parameters:
    m_a (list) - list of list of integers or float
    m_b (list) - list of list of integers or float
"""


def matrix_mul(m_a, m_b):
    """ Returns the product of two matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for item in m_a:
        if type(item) is not list:
            raise TypeError("m_a must be list of list")

    for item in m_b:
        if type(item) is not list:
            raise TypeError("m_b must be a list of list")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0] == 0)):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in range(len(row)):
            if type(row[elem]) not in [int, float]:
                raise TypeError("m_a should contain only integers or float")

    for row in m_b:
        for elem in range(len(row)):
            if type(row[elem]) not in [int, float]:
                raise TypeError("m_b should contain only integers or float")

    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    row_len = len(m_b)
    col_len = len(m_a[0])
    if row_len != col_len:
        raise ValueError("m_a and m_b can't be multiplied")

    nr = len(m_a)
    nc = len(m_a[0])
    prods = []

    for i in range(nr):
        row = []
        for j in range(nc):
            val = 0
            for k in range(nc):
                val += m_a[i][k] * m_b[k][j]
            row.append(val)
        prods.append(row)
    return prods
