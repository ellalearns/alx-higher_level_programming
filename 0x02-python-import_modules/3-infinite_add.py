#!/usr/bin/python3

if __name__ == "__main__":
    """infinite add - add all arguments"""
    from sys import argv

    args = len(argv)
    counter = 1
    total = 0

    if args == 1:
        total = 0
    else:
        while (counter < args):
            total += int(argv[counter])
            counter += 1

    print("{}".format(total))
