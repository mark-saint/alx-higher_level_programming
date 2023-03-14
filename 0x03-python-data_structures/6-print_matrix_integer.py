#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_ in matrix:
        for num in list_:
            print("{:d}".format(num), end='')
            if num != list_[-1]:
                print(end=' ')
        print()
