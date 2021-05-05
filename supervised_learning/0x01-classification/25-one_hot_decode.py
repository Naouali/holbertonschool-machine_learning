#!/usr/bin/env python3
"""
decode hot
"""


import numpy as np


def one_hot_decode(one_hot):
    if (one_hot > 1).all() or (one_hot < 0).all():
        return None
    if len(one_hot.shape) != 2:
        return None
    data = []
    for i in one_hot.T:
        data.append(np.argmax(i))
    return np.array(data)
