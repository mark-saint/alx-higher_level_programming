#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i, s in enumerate(str):
        if i == n:
            continue
        new_str += s
    return new_str
