#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(f"{i}")
    elif i < 10:
        print("{}".format("0" + str(i)), end=", ")
    else:
        print("{}".format(i), end=", ")
