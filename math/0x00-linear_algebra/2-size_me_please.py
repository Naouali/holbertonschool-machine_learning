#!/usr/bin/env python3
"""
determine the shape of a matrix
"""


def matrix_shape(matrix):
    """
    function to calculatre matrix shape
    """
    shape = []
    while type(matrix) is list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
