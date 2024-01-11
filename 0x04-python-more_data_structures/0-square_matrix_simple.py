#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) != 0:
        new_mat = []
        for i in range(len(matrix)):
            lst = []
            for j in range(len(matrix[i])):
                lst.append(matrix[i][j]**2)
            new_mat.append(lst)
        return (new_mat)
    return (matrix)
