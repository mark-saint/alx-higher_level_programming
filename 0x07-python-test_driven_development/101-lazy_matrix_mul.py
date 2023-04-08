#!/usr/bin/python3
"""
Module is so lazy to multiply
matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    :param m_a
    :param m_b
    """
    return np.matmul(m_a, m_b)
