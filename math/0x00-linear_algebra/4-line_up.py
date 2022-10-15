#!/usr/bin/env python3
"""
Add two 1D arrays element wise
"""


def add_arrays(arr1, arr2):
    """
    Input: Two 1D arrays
    Output: 1D array
    """
    if len(arr1) != len(arr2):
        return None
    else:
        added = []
        for i, j in zip(arr1, arr2):
            added.append(i + j)
        return added
