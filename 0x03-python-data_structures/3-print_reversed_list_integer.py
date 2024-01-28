#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    print the elements of a list
    in reversed order
    """
    if my_list is None:
        my_list = []

    counter = 0
    rev_counter = -1
    while counter in range(len(my_list)):
        print("{:d}".format(my_list[rev_counter]))
        rev_counter -= 1
        counter += 1
