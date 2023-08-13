#!/usr/bin/python3

def no_c(my_string):
    """removes all c's and C's from a string.

    Args:
        my_string: the string
    """
    if type(my_string) is str:
        strlist = [char for char in my_string]

        while "c" in strlist:
            del strlist[strlist.index("c")]

        while "C" in strlist:
            del strlist[strlist.index("C")]

        newstr = ""
        newstr2 = newstr.join(strlist)

        return newstr2
