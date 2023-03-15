#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        big_value = max(list(a_dictionary.values()))
        for key, value in a_dictionary.items():
            if value == big_value:
                return key
