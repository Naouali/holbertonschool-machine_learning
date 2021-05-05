#!/usr/bin/env python3
"""
decode hot 2D matrix
"""


import numpy as np


def one_hot_decode(one_hot):
    """
    decode a one hot matrix
    to one D array
    """
    if type(one_hot) is not np.ndarray:
        return None
    if (one_hot > 1).all() or (one_hot < 0).all():
        return None
    if len(one_hot.shape) != 2:
        return None
    data = []
    for i in one_hot.T:
        data.append(np.argmax(i))
    return np.array(data)
