#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    print the integers of a matrix
    """
    if matrix is None:
        print("", end="$\n")
    if matrix == [[]]:
        print("", end="$\n")
    for listd in matrix:
        counter = 0
        while counter < len(listd):
            if (counter == len(listd) - 1):
                print("{:d}".format(listd[counter]), end="$\n")
            else:
                print("{:d}".format(listd[counter]), end=" ")
            counter += 1
