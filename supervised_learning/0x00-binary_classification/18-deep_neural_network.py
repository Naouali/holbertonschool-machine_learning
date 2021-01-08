#!/usr/bin/env python3
"""
deep neural network class
"""

import numpy as np


class DeepNeuralNetwork:
    """
    Deep neuarl network class
    """
    def __init__(self, nx, layers):
        """
        deep neural network constructor
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list or not layers:
            raise TypeError("layers must be a list of positive integers")
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(len(layers)):
            if layers[i] <= 0:
                raise TypeError("layers must be a list of positive integers")
            if i == 0:
                self.__weights['W' + str(i + 1)
                               ] = np.random.randn(layers[i], nx) *\
                    np.sqrt(2/nx)
            else:
                self.__weights['W' + str(i + 1)] = \
                    np.random.randn(layers[i], layers[i-1]) * \
                    np.sqrt(2/layers[i-1])
            self.__weights['b' + str(i + 1)] = np.zeros((layers[i], 1))

    @property
    def L(self):
        """
        Number of layers getter
        """
        return self.__L

    @property
    def cache(self):
        """
        cache getter
        """
        return self.__cache

    @property
    def weights(self):
        """
        weights getter
        """
        return self.__weights

    def forward_prop(self, X):
        """
        forward propagation for deep neural network
        """
        self.__cache["A0"] = X
        for i in range(self.__L):
            W = self.__weights["W" + str(i + 1)]
            A = self.__cache["A" + str(i)]
            b = self.__weights["b" + str(i + 1)]
            z = np.dot(W, A) + b
            self.__cache["A" + str(i + 1)] = 1 / (1 + np.exp(-z))
        return self.__cache["A" + str(self.__L)], self.__cache
