#!/usr/bin/env python3
"""
normalize matrix
"""


import numpy as np


def normalize(X, m, s):
    """
    Normalize data
    """

    Norm = np.subtract(X, m) / s
    return Norm
