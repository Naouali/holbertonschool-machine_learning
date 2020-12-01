#!/usr/bin/env python3
"""
module to add matrices
"""


def shape(matrix):
    """
    calculate shape of matrix
    """
    shape = []
    while type(matrix) is list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


def add_array(arr1, arr2):
    return [i + j for i, j in zip(arr1, arr2)]


def add_matrices2D(mat1, mat2):
    """
    add two matrices elements-wise
    """
    if shape(mat1) != shape(mat2):
        return None
    m = []
    for i, j in zip(mat1, mat2):
        m.append(add_array(i, j))
    return m
