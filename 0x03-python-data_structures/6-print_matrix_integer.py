#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_matrix = len(matrix)
    for i in range(len_matrix):
        len_row = len(matrix[i])
        for j in range(len_row):
            print(matrix[i][j], end=' ')
            if j == 2:
                print()
