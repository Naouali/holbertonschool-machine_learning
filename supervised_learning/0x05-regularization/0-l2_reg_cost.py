#!/usr/bin/env python3
"""
l2 regularization
"""


import numpy as np


def l2_reg_cost(cost, lambtha, weight, L, m):
    """
    L2 regularization
    """
    s = 0
    for i in range(L):
        s += np.linalg.norm(weight['W' + str(i + 1)])
    return cost + s * lambtha * 0.5 / m
