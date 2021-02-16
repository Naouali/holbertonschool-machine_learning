#!/usr/bin/env python3
"""
normal
"""

import numpy as np


def normalization_constants(X):
    """
    Normalize a matrix
    """
    mean = np.sum(X / X.shape[0], axis=0)
    std = np.sqrt(np.sum(((X - mean) ** 2), axis=0) / X.shape[0])
    return mean, std
