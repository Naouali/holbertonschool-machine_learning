#!/usr/bin/env python3
"""
one hot encoder
"""


import numpy as np


def one_hot_encode(Y, classes):
    """
    encode
    """
    if Y is None or classes is None:
        return None
    if len(Y) == 0:
        return None
    if classes < 0:
        return None
    if Y.max() >= classes:
        return None
    hot = np.zeros((Y.shape[0], classes))
    for i in Y:
        j = np.where(Y == i)
        hot[i][j] = 1
    return hot
