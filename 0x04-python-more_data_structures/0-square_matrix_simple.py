#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Returns a new list \
    with square value integers of all integers of a matrix
    """
    new_matrix = matrix
    final_matrix = []
    for seq in new_matrix:
        if type(seq) is list:
            new_seq = list(map(lambda x: x**2, seq))
            final_matrix.append(new_seq)
        elif type(seq) is int:
            new_int = seq**2
            final_matrix.append(new_int)
    return final_matrix
