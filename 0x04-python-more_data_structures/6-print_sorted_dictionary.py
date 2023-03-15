#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(list(a_dictionary.keys()))
    for sorted_key in sorted_keys:
        print("{}: {}".format(sorted_key, a_dictionary[sorted_key]))
