#!/usr/bin/env python3
"""
module to add two arrays elements wise
"""


def add_arrays(arr1, arr2):
    """
    function to add two array
    """
    if len(arr1) is not len(arr2):
        return None
    ziped = []
    for i, j in zip(arr1, arr2):
        ziped.append(i+j)
    return ziped
