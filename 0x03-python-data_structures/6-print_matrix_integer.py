#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_ in matrix:
        for l in list_:
            print("{:d}".format(l), end=' ')
        print()
