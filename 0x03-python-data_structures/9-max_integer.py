#!/usr/bin/python3
def max_integer(my_list=[]):
    largest_num = 0
    for i in my_list:
        if i > largest_num:
            largest_num = i

    return largest_num
