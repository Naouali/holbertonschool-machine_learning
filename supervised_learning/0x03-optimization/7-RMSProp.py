#!/usr/bin/env python3
"""
RMSProp
"""


import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """
    RMSProp
    """
    dw = beta2 * s + (1 - beta2) * (grad ** 2)
    w = var - alpha * grad / (dw ** 0.5 + epsilon)
    return w, dw
