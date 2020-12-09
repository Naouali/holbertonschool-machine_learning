#!/usr/bin/env python3
"""
summation
"""


def summation_i_squared(n):
    """
    n: stopping condition
    return: total
    """
    if type(n) != int:
        return None
    return int(n / 6 + (n ** 2) / 2 + pow(n, 3) / 3)
