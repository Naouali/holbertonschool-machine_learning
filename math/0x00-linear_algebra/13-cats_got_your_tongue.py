#!/usr/bin/env python3
"""
module to concate matrcies
"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    function to concate mat1, mat2 on axis
    """
    return np.concatenate((mat1, mat2), axis)
