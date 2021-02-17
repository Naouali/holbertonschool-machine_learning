#!/usr/bin/env python3
"""
Norm
"""


import numpy as np


def normalization_constants(X):
	"""
	normalizing
	"""
	m = X.shape[0]
	mean = np.sum(X/ m, axis=0)
	std = np.sqrt(np.sum(((X - mean) ** 2), axis=0) / m)
	return mean, std
