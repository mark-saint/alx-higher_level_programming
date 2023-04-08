#!/usr/bin/python3
"""
Module to multiply 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply 2 matrices
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError("m_b should only contain integers or floats")

    len_lists_a = set(list(map(lambda x: len(x), m_a)))
    if len(len_lists_a) != 1:
        raise TypeError("each row of m_a must be of the same size")

    len_lists_b = set(list(map(lambda x: len(x), m_b)))
    if len(len_lists_b) != 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for r in m_a:
        nr = []
        d = 0
        while d < len(m_b[0]):
            k = 0
            res = 0
            for c in r:
                res += (c * m_b[k][d])
                k += 1
            nr.append(res)
            d += 1
        new_matrix.append(nr)

    return new_matrix
