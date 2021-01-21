#!/usr/bin/env python3
"""
Normal distriution
"""


class Normal:
    """
    Normal distribution class
    """
    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            self.mean = float(mean)
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.stddev = float(stddev)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            std = 0
            for i in data:
                std += (i - self.mean) ** 2
            std = std / len(data)
            self.stddev = std ** (1/2)

    def z_score(self, x):
        """
        z_score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        calculate the x value of z_score
        """
        return (z * self.stddev) + self.mean

    def root(self, n):
        """
        return square root of n
        """
        return n ** (1/2)

    def pdf(self, x):
        """
        probability density function
        """
        pi = 3.1415926536
        e = 2.7182818285
        s = self.stddev
        return e ** ((-1/2) * self.z_score(x) ** 2) / (s * self.root(2 * pi))

    def cdf(self, x):
        """
        comulative distribution function
        """
        return (1 + self.erf(self.z_score(x) / self.root(2))) / 2

    def erf(self, x):
        """
        error
        """
        pi = 3.1415926536
        one = x
        two = (x ** 3) / 3
        three = (x ** 5) / 10
        four = (x ** 7) / 42
        five = (x ** 9) / 216
        return 2 * (one - two + three - four + five) / self.root(pi)
