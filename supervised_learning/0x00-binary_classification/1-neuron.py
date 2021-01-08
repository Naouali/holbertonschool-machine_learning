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
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        get weight of the neuron
        """
        return self.__W

    @property
    def b(self):
        """
        get bias of the neuron
        """
        return self.__b

    @property
    def A(self):
        """
        get output of the neuron
        """
        return self.__A
