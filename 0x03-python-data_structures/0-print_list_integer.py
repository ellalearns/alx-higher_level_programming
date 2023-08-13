#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Function to print integers in list.
    Assuming all entries are integers.

    Args:
        my_list: the list of integers

    Returns:
        void

    """
    for int in my_list:
        print("{:d}".format(int))
