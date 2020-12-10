#!/usr/bin/env python3
"""
module to calculate derivatives
"""


def poly_derivative(poly):
    """
    args: polynomial
    return: derivatoive
    """
    if isinstance(poly, list) is False or len(poly) == 0:
        return None
    derivatives = []
    for i in range(len(poly)):
        if type(poly[i]) != int and type(poly[i]) != float:
            return
        if i != 0:
            derivatives.append(i * poly[i])
    return derivatives
