#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        for i, element in enumerate(my_list):
            if element == search:
                my_list[i] = replace
    return my_list
