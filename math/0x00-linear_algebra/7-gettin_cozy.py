#!/usr/bin/env python3
"""
module to concate matrices on specific axes
"""



def cat_matrices2D(mat1, mat2, axis=0):
    """
    args: two matrices and axies
    return: matrix
    """
    if axis == 0:
        if len(mat1[0]) is not len(mat2[0]):
            return None
        return [item.copy() for item in mat1] + [item.copy() for item in mat2]
    else:
        if len(mat1) is not len(mat2):
            return None
        return [item.copy() + item2.copy() for item, item2 in zip(mat1, mat2)]
