#!/usr/bin/env python3
"""
bionomial class
"""


class Binomial:
    """
    binomial class
    """
    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p < 0 or p > 1:
                raise ValueError("p must e greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.p = (sum(data) / len(data)) / len(data)
            self.n = int(round(len(data)))
            self.p = (sum(data)/len(data) / self.n) * 2
