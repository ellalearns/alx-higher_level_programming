#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:0=2d}{} ".format(num, ','), end="")
