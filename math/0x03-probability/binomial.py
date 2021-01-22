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
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = 0
            for i in data:
                variance += (i - mean) ** 2
            variance = variance / len(data)
            self.p = -1 * (variance / mean - 1)
            self.n = round(mean / self.p)
            self.p = mean / self.n

    def pmf(self, k):
        """
        pmf of binomail
        """
        def factorial(n):
            """
            return factorial of n
            """
            if n == 0:
                return 1
            if n == 1:
                return 1
            return n * factorial(n - 1)
        k = int(k)
        if k < 0:
            return 0
        part1 = factorial(self.n) / (factorial(k) * (factorial(self.n - k)))
        part2 = self.p ** k * ((1 - self.p) ** (self.n - k))
        return part1 * part2

    def cdf(self, k):
        """
        cdf binomial
        """
        if k < 0:
            return 0
        k = int(k)
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
