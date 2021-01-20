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

    def pmf(self, k):
        """
        Probability mass function
        """
        def factorial(n):
            """
            calculate factoril
            """
            if n == 0:
                return 0
            if n == 1:
                return 1
            return n * factorial(n - 1)
        e = 2.7182818285
        k = int(k)
        if k < self.lambtha:
            return 0
        p = (self.lambtha ** k) * (e ** (-1 * self.lambtha))
        return p / factorial(k)

    def cdf(self, k):
        """
        probability comulative function
        """
        def f(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            return n * f(n - 1)
        e = 2.7182818285
        cdf = 0
        for i in range(0, k + 1):
            cdf += (self.lambtha ** i) / f(i)
        cdf = cdf * (e ** (-1 * self.lambtha))
        return cdf
