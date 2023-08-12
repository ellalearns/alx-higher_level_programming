#!/usr/bin/python3
if __name__ == "__main__":
    """print all arguments used to run program"""
    from sys import argv

    args = len(argv)

    if args == 1:
        print("{} arguments.".format(args - 1))
    elif args == 2:
        print("{} argument:".format(args - 1))
    else:
        print("{} arguments:".format(args - 1))

    if args >= 2:
        arg = 1
        while arg < args:
            print("{}: {}".format(arg, argv[arg]))
            arg += 1
