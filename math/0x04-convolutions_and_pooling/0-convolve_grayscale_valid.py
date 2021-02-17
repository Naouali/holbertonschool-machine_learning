#!/usr/bin/env python3
"""
perform a convolution
"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    perform a convolution
    """

    m, h, w = images.shape
    kh, kw = kernel.shape
    cvns = np.zeros((m, int(h - kh + 1), int(w - kw + 1)))

    for i in range(h - kh + 1):
        for j in range(w - kw + 1):
            cvns[:, i, j] = np.sum(
                images[:, i: i + kh, j: j + kw] * kernel, axis=(1, 2))
    return cvns
