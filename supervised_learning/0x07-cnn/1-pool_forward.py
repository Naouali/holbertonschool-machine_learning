#!/usr/bin/env python3
"""Convolution Neural Network module"""
import numpy as np


def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """
    CNN
    """
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    output_h = int((h_prev - kh) / sh + 1)
    output_w = int((w_prev - kw) / sw + 1)

    if mode == "max":
        pool_operation = np.max
    else:
        pool_operation = np.average

    output = np.zeros((m, output_h, output_w, c_prev))
    for i in range(output_h):
        for j in range(output_w):
            output[:, i, j, :] = pool_operation(
                A_prev[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :],
                axis=(1, 2)
            )
    return output
