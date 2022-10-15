#!/usr/bin/env python3
"""
transpose a matrix
"""


def matrix_transpose(matrix):
    """
    Input: matrix
    Output: matrix transposed
    """
    transposed = []
    for x in matrix:
        transposed.append([])

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transposed[i].append(matrix[j][i])
    return transposed
