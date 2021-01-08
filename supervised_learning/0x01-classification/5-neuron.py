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

    def evaluate(self, X, Y):
        """
        evaluate the performance of the neuron
        """
        A = self.forward_prop(X)
        ones = np.where(A >= 0.5, 1, 0)
        cost = self.cost(Y, A)
        return ones, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        add gradient descent
        """
        features = X.shape[1]
        d = A - Y
        weight_d = np.sum(X * d, axis=1)
        bais_d = np.sum(d)

        self.__W = self.__W - (alpha * (weight_d / features))
        self.__b = self.__b - (alpha * (bais_d / features))
