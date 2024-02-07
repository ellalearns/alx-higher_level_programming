#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    divides element by element in 2 lists
    """
    counter = 0
    new_list = []
    while counter < list_length:
        try:
            result = my_list_1[counter] / my_list_2[counter]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
            counter += 1
    return new_list
