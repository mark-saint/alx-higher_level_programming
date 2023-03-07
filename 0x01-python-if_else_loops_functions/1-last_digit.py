#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


last_n = str(number)

last_n = last_n[-1]
last_int = int(last_n)
if number < 0:
    last_int = -1 * last_int
if last_int > 5:
    print(f"Last digit of {number} is {last_n} and is greater than 5")
elif last_int == 0:
    print(f"Last digit of {number} is {last_n} and is 0")
elif last_int < 6 and last_int != 0:
    print(f"Last digit of {number} is {last_int} and is less than 6 and not 0")

else:
    print()
