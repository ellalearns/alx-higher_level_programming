#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique ints in a list

    Args:
        my_list: the list of integers

    Returns:
        int: sum of all unique ints in the list
    """
    new_list = my_list
    mto = []
    added = []
    total = 0

    for x in new_list:
        if new_list.count(x) > 1:
            if x not in mto:
                mto.append(x)

    for x in new_list:
        if x in mto:
            if x not in added:
                total += x
                added.append(x)
        else:
            total += x

    return total
