#!/usr/bin/python3
def safe_print_list_integers(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    else: 
        return True
