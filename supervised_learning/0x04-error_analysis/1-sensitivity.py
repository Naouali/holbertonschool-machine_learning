#!/usr/bin/env python3
"""
sensitivity
"""
import numpy as np


def sensitivity(confusion):
    """
    sensitivity
    """
    m = np.diagonal(confusion)
    return (m / confusion.sum(axis=1))
