#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len_ = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            len_ += 1
        except IndexError:
            break
        print()
        return len_
