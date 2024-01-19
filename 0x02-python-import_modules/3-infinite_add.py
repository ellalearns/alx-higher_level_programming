#!/usr/bin/python3

if __name__ == "__main__":
    """
    prints the result of the addition of all arguments
    """
    import sys

    argv = sys.argv
    total = 0

    if len(argv) > 1:
        total = 0
        index = 1

        while (index < len(argv)):
            total += int(argv[index])
            index += 1
    
    print("{}".format(total))
