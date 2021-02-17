#!/usr/bin/env python3
"""
<<<<<<< HEAD
Norm
"""


=======
normal
"""

>>>>>>> 982c764c6b1edb6530c5d08930d5fd2f637ec485
import numpy as np


def normalization_constants(X):
<<<<<<< HEAD
	"""
	normalizing
	"""
	m = X.shape[0]
	mean = np.sum(X/ m, axis=0)
	std = np.sqrt(np.sum(((X - mean) ** 2), axis=0) / m)
	return mean, std
=======
    """
    Normalize a matrix
    """
    mean = np.sum(X / X.shape[0], axis=0)
    std = np.sqrt(np.sum(((X - mean) ** 2), axis=0) / X.shape[0])
    return mean, std
>>>>>>> 982c764c6b1edb6530c5d08930d5fd2f637ec485
