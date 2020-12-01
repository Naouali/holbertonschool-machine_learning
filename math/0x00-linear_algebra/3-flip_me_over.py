#!/usr/bin/env python3
"""
Module to transpose a matrix
"""


def matrix_transpose(matrix):
    """
    function to transpose a matrix
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
