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
    if type(classes) is not int or type(Y) is not np.ndarray:
        return None
    if classes < 0:
        return None
    if Y.max() >= classes:
        return None
    hot = np.zeros((classes, len(Y)))
    count = -1
    for i in Y:
        count += 1
        hot[i][count] = 1
    return hot
