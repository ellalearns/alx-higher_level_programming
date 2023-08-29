#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    divides element by element in two lists
    :param my_list_1: first list
    :param my_list_2: second list
    :param list_length: list length
    :return: new list
    """
    counter = 0
    result = 0
    new_list = []
    while counter < list_length:
        try:
            result = my_list_1[counter] / my_list_2[counter]
        except (TypeError, ValueError):
            result = 0
            print("wrong type", end="\n")
        except ZeroDivisionError:
            result = 0
            print("division by 0", end="\n")
        except IndexError:
            print("out of range", end="\n")
            return new_list
        finally:
            new_list.append(result)
            counter += 1

    return new_list
