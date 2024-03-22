#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s_matrix = []
    for row in matrix:
        s_row = []
        for column in row:
            s_row.append(column ** 2)
        s_matrix.append(s_row)
    return s_matrix
