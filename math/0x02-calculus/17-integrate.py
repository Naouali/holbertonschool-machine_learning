#!/usr/bin/env python3
"""
module to calculate the integral of polynomial
"""


def poly_integral(poly, C=0):
    """
    args: polynomial arr and constant
    return: array of antiderivatives
    """
    if not isinstance(poly, list) or not isinstance(C, int) or (not poly):
        return None
    if poly == [0]:
        return None
    if poly != [0]:
        integrals = poly[:]
    else:
        intgerals = []
    integrals.insert(0, C)
    for i in range(1, len(integrals)):
        if integrals[i] != 0:
            integrals[i] /= i
            if integrals[i] == int(integrals[i]):
                integrals[i] = int(integrals[i])
    return integrals
