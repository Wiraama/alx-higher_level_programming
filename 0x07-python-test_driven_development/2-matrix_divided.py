#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix. """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    row_size = len(matrix[0])

    new_matrix = []
    for row in matrix:
        results = []
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                result = element / div
                result = f"{result:.2f}"
                results.append(result)
        new_matrix.append(results)
    return new_matrix
