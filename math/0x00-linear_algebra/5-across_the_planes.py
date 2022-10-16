#!/usr/bin/env python3
"""
add two matrices element wise
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


def add_arrays(arr1, arr2):
    """
    Input: Two 1D arrays
    Output: 1D array
    """
    if len(arr1) != len(arr2):
        return None
    else:
        added = []
        for i, j in zip(arr1, arr2):
            added.append(i + j)
        return added


def add_matrices2D(mat1, mat2):
    """
    add two matrices element wise
    """
    added = []
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    else:
        for x, j in zip(mat1, mat2):
            added.append(add_arrays(x, j))
    return added
