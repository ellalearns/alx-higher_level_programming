#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0 or number == 0:
    last_digit = str(number)[-1]
else:
    last_digit = str(number)[0] + str(number)[-1]
    if last_digit == "-0":
        last_digit = 0

last_string = ""

if int(last_digit) > 5:
    last_string = "greater than 5"
elif int(last_digit) == 0:
    last_string = "0"
elif int(last_digit) < 6 and int(last_digit) != 0:
    last_string = "less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} and is {last_string}")
