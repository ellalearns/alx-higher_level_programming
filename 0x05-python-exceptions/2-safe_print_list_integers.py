#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    safely print list integers
    """
    counter = 0
    another_one = 0
    handle = 0

    list_elems = 0
    for elem in my_list:
        list_elems += 1

    if x > list_elems:
        raise IndexError("list index out of range")

    while another_one < x:
        try:
            print("{:d}".format(my_list[another_one]), end="")
            counter += 1
        except Exception:
            pass
        finally:
            another_one += 1
    print("")
    return counter
