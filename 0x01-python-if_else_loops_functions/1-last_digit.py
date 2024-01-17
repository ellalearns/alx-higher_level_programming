#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
first_str = "Last digit of"
second_str = ""
last_digit = 0
if number >= 0:
    last_digit = int(str(number)[-1])
else:
    last_digit = 0 - int(str(number)[-1])
if last_digit > 5:
    second_str = "and is greater than 5"
elif last_digit == 0:
    second_str = "and is 0"
elif last_digit < 6 and last_digit != 0:
    second_str = "and is less than 6 and not 0"
print(f"{first_str} {number} is {last_digit} {second_str}")
