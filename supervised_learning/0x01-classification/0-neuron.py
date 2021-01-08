#!/usr/bin/env python3
"""
module to create a neuron for ANN
"""


import numpy as np


class Neuron:
    """
    Neuron class
    """
    def __init__(self, nx):
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
