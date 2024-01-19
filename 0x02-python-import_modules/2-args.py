#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    len_argv = len(argv) - 1
    if len_argv == 0:
        print("{} arguments.".format(len_argv))
    elif len_argv == 1:
        print("{} argument:".format(len_argv))
        print("{}: {}".format(len_argv, argv[1]))
    else:
        print("{} arguments:".format(len_argv))
        counter = 1
        while counter <= len_argv:
            print("{}: {}".format(counter, argv[counter]))
            counter += 1
