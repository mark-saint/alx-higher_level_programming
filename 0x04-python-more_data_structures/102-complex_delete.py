#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    values_ = list(a_dictionary.values())
    if value not in values_:
        return a_dictionary
    new_dict = a_dictionary.copy()
    for key, value_ in new_dict.items():
        if value_ == value:
            a_dictionary.pop(key)
    return a_dictionary
