#!/usr/bin/python3

def best_score(a_dictionary):
    """return the key with the highest int
    """
    if type(a_dictionary) is not dict:
        return None
    if len(a_dictionary) < 1:
        return None
    else:
        high_score = 0
        for key in a_dictionary:
            if a_dictionary[key] > high_score:
                high_score = a_dictionary[key]

    return high_score
