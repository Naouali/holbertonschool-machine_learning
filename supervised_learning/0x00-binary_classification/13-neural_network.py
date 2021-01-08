#!/usr/bin/env python3
"""
module to create a neural network
"""


import numpy as np


class NeuralNetwork:
    """
    Neutal network class
    """
    def __init__(self, nx, nodes):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """
        W1 getter
        """
        return self.__W1

    @property
    def b1(self):
        """
        b1 getter
        """
        return self.__b1

    @property
    def A1(self):
        """
        A1 getter
        """
        return self.__A1

    @property
    def W2(self):
        """
        W2 getter
        """
        return self.__W2

    @property
    def b2(self):
        """
        b2 getter
        """
        return self.__b2

    @property
    def A2(self):
        """
        A2 getter
        """
        return self.__A2

    def forward_prop(self, X):
        """
        forward propagation function of neural network
        activation + sigmoid function
        return __A1,__A2
        """
        activation1 = np.dot(self.__W1, X) + self.__b1
        sigmoid1 = 1 / (1 + np.exp(-activation1))
        self.__A1 = sigmoid1
        activation2 = np.dot(self.__W2, self.__A1) + self.__b2
        sigmoid2 = 1 / (1 + np.exp(-activation2))
        self.__A2 = sigmoid2
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """
        cost function of neural network
        """
        cost = -(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)).mean()
        return cost

    def evaluate(self, X, Y):
        """
        evalute the performance of the neural network
        """
        _, A = self.forward_prop(X)
        ones = np.where(A >= 0.5, 1, 0)
        cost = self.cost(Y, A)
        return ones, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        gradient descent to upgate W1, W2, b1, b2
        """
        m = X.shape[1]
        dz2 = A2 - Y
        dw2 = np.matmul(dz2, A1.T) / m
        db2 = np.sum(dz2, axis=1, keepdims=True) / m

        dz1 = np.matmul(self.__W2.T, dz2) * (A1 * (1 - A1))
        dw1 = np.matmul(dz1, X.T) / m
        db1 = np.sum(dz1, axis=1, keepdims=True) / m

        self.__W1 = self.__W1 - alpha * dw1
        self.__W2 = self.__W2 - alpha * dw2
        self.__b1 = self.__b1 - alpha * db1
        self.__b2 = self.__b2 - alpha * db2
