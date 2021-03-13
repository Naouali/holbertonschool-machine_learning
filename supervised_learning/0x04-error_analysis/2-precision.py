#!/usr/bin/env python3
"""
precision
"""


import numpy as np


def precision(confusion):
    """
    precision
    """
    m = np.diagonal(confusion)
    return (m / confusion.sum(axis=0))
