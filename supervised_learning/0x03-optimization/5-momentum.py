#!/usr/bin/env python3
"""
momentum
"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """
    Create momentum
    """
    dw = beta1 * v + (1 - beta1) * grad
    w = var - alpha * dw
    return w, dw
