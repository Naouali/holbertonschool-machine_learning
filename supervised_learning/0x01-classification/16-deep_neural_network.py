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
        self.L = len(layers)
        self.cache = {}
        self.weights = {}
        for i in range(len(layers)):
            if layers[i] <= 0:
                raise TypeError("layers must be a list of positive integers")
            if i == 0:
                self.weights['W' + str(i + 1)
                             ] = np.random.randn(layers[i], nx) * np.sqrt(2/nx)
            else:
                self.weights['W' + str(i + 1)] = \
                    np.random.randn(layers[i], layers[i-1]) * \
                    np.sqrt(2/layers[i-1])
            self.weights['b' + str(i + 1)] = np.zeros((layers[i], 1))
