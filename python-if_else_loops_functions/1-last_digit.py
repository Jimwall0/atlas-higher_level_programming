#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    lword = number % 10
    number = number * -1
else:
    lword = number % 10
if lword > 5:
    print(f"Last digit of {number} is {lword} and is greater than 5")
elif lword == 0:
    print(f"Last digit of {number} is {lword} and is 0")
else:
    print(f"Last digit of {number} is {lword} and is less than 6 and not 0")
