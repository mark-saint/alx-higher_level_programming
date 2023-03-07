#!/usr/bin/python3
def uppercase(str):
    upper_nums = list(range(65, 91))
    lower_nums = list(range(97, 123))
    new_str = ""

    for i in str:
        if ord(i) in upper_nums:
            new_str += i
        elif ord(i) in lower_nums:
            new_str += chr(ord(i) - 32)
        else:
            new_str += i
    print("{}".format(new_str))
