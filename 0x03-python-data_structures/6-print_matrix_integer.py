#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """print the integers in a matrix.
    Assuming all the elements in the matrix are integers.

    Args:
        matrix: the matrix list

    Returns:
        null
    """
    for matrium in matrix:
        for elem in matrium:
            if matrium.index(elem) == len(matrium) - 1:
                print("{:d}".format(elem), end="\n")
            else:
                print("{:d}".format(elem), end=" ")
