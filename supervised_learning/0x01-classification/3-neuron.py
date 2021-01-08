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

    def forward_prop(self, X):
        """
        forward propagation of the neuron
        args: x is np.ndarray with shape(nx, m)
        nx = input features
        m = training example
        """

        output = np.matmul(self.__W, X) + self. __b
        output_segmoid = 1 / (1 + np.exp(-output))
        self.__A = output_segmoid
        return self.__A

    def cost(self, Y, A):
        """
        cost function to determine the error of the NN
        args: Y the correct labels of the data
            A the output of the neuron
        """
        cost = - ((Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))).mean()

        return cost
