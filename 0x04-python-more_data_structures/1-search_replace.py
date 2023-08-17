#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replace all occurrences \
    of an element in a list
    """
    new_list = my_list
    if type(new_list) is not list:
        return None
    else:
        if search is None or replace is None:
            return new_list
        else:
            n_l = list(map(lambda x: replace if x == search else x, new_list))

    return n_l
