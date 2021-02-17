#!/usr/bin/env python3
"""
Moving average
"""


import numpy as np


def moving_average(data, beta):
    """
    Moving average function
    """
    MVA = []
    v = 0
    for i in range(len(data)):
        v = beta * v + (1 - beta) * data[i]
        MVA.append(v / (1 - beta ** (i + 1)))
    return MVA
