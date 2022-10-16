#!/usr/bin/env python3
"""
add two matrices element wise
"""


def add_arrays(arr1, arr2):
    """
    Input: Two 1D arrays
    Output: 1D array
    """
    added = []
    for i, j in zip(arr1, arr2):
        added.append(i + j)
    return added


def add_matrices2D(mat1, mat2):
    """
    add two matrices element wise
    """
    added = []
    if len(mat1[0]) != len(mat2[0]):
        return None
    else:
        for x, j in zip(mat1, mat2):
            added.append(add_arrays(x, j))
    return added
