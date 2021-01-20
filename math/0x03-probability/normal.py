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
