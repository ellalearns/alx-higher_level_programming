#!/usr/bin/python3
if __name__ == "__main__":
    """
    imports an add function
    adds two variables together
    """
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
