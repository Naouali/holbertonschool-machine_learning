#!/usr/bin/env python3
"""
Poisson distribution
"""


class Poisson:
    """
    Poisson distribution class
    """
    def __init__(self, data=None, lambtha=1.):
        self.lambtha = float(lambtha)
        if data is None:
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)
