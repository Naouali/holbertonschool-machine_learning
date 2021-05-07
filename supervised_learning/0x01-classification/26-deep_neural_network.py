#!/usr/bin/env python3
"""
deep neural network class
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle


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

    def cost(self, Y, A):
        """
        cost of deep neural network
        """
        cost = -(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)).mean()
        return cost

    def evaluate(self, X, Y):
        """
        evaluate deep neural netwrok
        """
        output, _ = self.forward_prop(X)
        A = np.where(output >= 0.5, 1, 0)
        cost = self.cost(Y, output)
        return A, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        """
        fradient descent for deep neural network
        """
        w = self.__weights.copy()
        m = self.__cache["A0"].shape[1]
        length = self.__L
        A, _ = self.forward_prop(self.__cache["A0"])
        dZ = A - Y

        for i in range(self.__L - 1, -1, -1):
            A = self.__cache["A" + str(i)]

            dW = np.dot(dZ, A.T) / m
            db = np.sum(dZ, axis=1, keepdims=True) / m
            self.__weights["W" + str(i+1)] = \
                self.__weights["W" + str(i+1)] - (alpha * dW)
            self.__weights["b" + str(i+1)] = \
                self.__weights["b" + str(i+1)] - (alpha * db)
            dZ = np.dot(
                w["W" + str(i+1)].T, dZ) * (A * (1 - A))

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """
        train the model
        """
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if verbose is True and graph is True:
            if type(step) is not int:
                raise TypeError("step must be an integer")
            if step < 0 and step > iterations:
                raise ValueError("step must be positive and <= iterations")
        costs = []
        itr = []
        for i in range(iterations + 1):
            A, A1 = self.forward_prop(X)
            self.gradient_descent(Y, A1, alpha)
            cost = self.cost(Y, A)
            if verbose is True:
                if i == 0 or i == iterations + 1 or i % step == 0:
                    print("Cost after {} iterations: {}".format(
                        i, cost
                    ))
            if graph is True:
                itr.append(i)
                costs.append(cost)
        plt.plot(itr, costs)
        plt.title("Trainig Cost")
        plt.xlabel("iteration")
        plt.ylabel("cost")
        plt.show()
        return self.evaluate(X, Y)

    def save(self, filename):
        """
        Function to save a model
        """
        if not(filename.endswith(".pkl")):
            filename = filename + ".pkl"
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        """
        function to load a pretrained parameters
        """
        try:
            with open(filename, "rb") as f:
                model = pickle.load(f)
            return model
        except FileNotFoundError:
            return None
