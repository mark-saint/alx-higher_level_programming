#!/usr/bin/python3
"""
the function in this
file divided all elements of
a matrix
"""


def matrix_divided(matrix, div):
    """
    :param matrix
    :param div
    Returns a new matrix
    """
    
    matrix_flat = [i for j in matrix for i in j]

    matrix_types = list(map(lambda x: type(x), matrix_flat))
    if str in matrix_types:
        raise TypeError("matrix must be a matrix list of lists) of integers/floats")
        
    len_ = []
    for l in matrix:
        len_.append(len(l))
    if len(set(len_)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix))

    return new_matrix
