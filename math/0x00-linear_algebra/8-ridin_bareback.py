#!/usr/bin/env python3
"""
module to perform matrix multiplication
"""


def transpose(matrix):
    """
    function to transpose a matrix
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def mul_array(arr1, arr2):
    """
    function to multiply arrays
    """
    return [x * y for x, y in zip(arr1, arr2)]


def mat_mul(mat1, mat2):
    """
    function to perform matrices multiplication
    """
    if len(mat1[0]) != len(mat2):
        return None
    t = transpose(mat2)
    return [[sum(mul_array(arr1, arr2)) for arr2 in t] for arr1 in mat1]
