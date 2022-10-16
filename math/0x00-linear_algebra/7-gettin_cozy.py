#!/usr/bin/env python3
"""
Concatinate along specific axe
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatinate along specific axe
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    else:
        if len(mat1) != len(mat2):
            return None
        m = []
        for x, y in zip(mat1, mat2):
            m.append(x + y)
        return m
