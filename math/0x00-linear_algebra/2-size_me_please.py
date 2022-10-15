#!/usr/bin/env python3
"""
Calculate shape of matrix
"""


def matrix_shape(matrix):
    """
    Input : 2D array
    Output: 1D Array shape of matrix
    """

    shape = []

    while type(matrix) is not int:
        shape.append(len(matrix))
        matrix = matrix[1]

    return shape