#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    n_sum = 0
    d_sum = 0
    for tup_ in my_list:
        n_sum += (tup_[0] * tup_[1])
        d_sum += tup_[1]
    return n_sum/d_sum
