#!/usr/bin/env python3
"""
Exponential distribution
"""


class Exponential:
    """
    Exponential class
    """
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            self.lambtha = float(lambtha)
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data) / len(data))

    def pdf(self, x):
        """
        Pdf of an exponential distribution
        """
        if x < 0:
            return 0
        e = 2.7182818285
        return self.lambtha * (e ** (-1 * self.lambtha * x))

    def cdf(self, x):
        """
        comulative function
        """
        if x < 0:
            return 0
        e = 2.7182818285
        return 1 - (e ** (-1 * self.lambtha * x))
