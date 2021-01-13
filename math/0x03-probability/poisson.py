#!/usr/bin/env python3
"""
Poisson distribution
"""


import numpy as np


class Poisson:
    def __init__(self, data=None, lambtha=1.):
        if not data:
            self.lambtha = float(lambtha)
            if self.lambtha < 0:
                raise ValueError("lambtha must be positive")
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = np.mean(data)
