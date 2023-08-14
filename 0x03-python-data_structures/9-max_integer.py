#!/usr/bin/python3

def max_integer(my_list=[]):
    """returns the biggest integer in a list

    Args:
        my_list: the list of integers

    Returns:
        the highest integer in the list
    """
    if len(my_list) == 0 or my_list is None or type(my_list) is not list:
        return None

    else:
        max_int = my_list[0]

        for int in my_list:
            if int > max_int:
                max_int = int

        return max_int
