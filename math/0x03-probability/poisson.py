#!/usr/bin/env python3
"""
Python program to generate the poisson distribution
"""


class Poisson:
    """
    Poisson Class
    """
    def __init__(self, data=None, lambtha=1.):
        """_summary_

        Args:
            data (List, optional): _description_. Defaults to None.
            lambtha (float, optional): _description_. Defaults to 1..
        """
        self.data = data
        self.lambtha = float(lambtha)
        if data is None:
            self.data = self.lambtha
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = sum(self.data) / len(self.data)
