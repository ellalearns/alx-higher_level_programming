#!/usr/bin/python3

"""
divides all the elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all the elements of a matrix
    all elements are lists of integers
    """
    terror = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []

    if matrix == []:
        new_matrix = matrix
        return new_matrix

    for elem in matrix:
        if isinstance(elem, list) is not True:
            raise TypeError(terror)
        else:
            for num in elem:
                if not (isinstance(num, int)) and not (isinstance(num, float)):
                    raise TypeError(terror)

    original_len = len(matrix[0])

    for elem in matrix:
        if len(elem) != original_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == int(0) or div == float(0):
        raise ZeroDivisionError("division by zero")

    for elem in matrix:
        elem_list = []
        for num in elem:
            result = round(num / div, 2)
            elem_list.append(result)
        new_matrix.append(elem_list)

    return new_matrix
