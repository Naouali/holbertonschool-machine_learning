#!/usr/bin/env python3
"""
shuffle data
"""


import numpy as np


def shuffle_data(X, Y):
    """
    shuffle data
    """
    p = np.random.permutation(len(X))
    return X[p], Y[p]
