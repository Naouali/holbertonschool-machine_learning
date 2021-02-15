#!/usr/bin/env python3
"""
one hot encoder
"""


import numpy as np


def one_hot_encode(Y, classes):
    """
    encode
    """

    hot = np.zeros((classes, classes))
    j = 0
    for i in Y:
        hot[i][j] = 1
        j += 1
    return hot
