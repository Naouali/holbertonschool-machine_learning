#!/usr/bin/env python3
"""
convilve
"""


import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Performs a same convolution on grayscale images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    p_l = pw
    p_r = pw
    p_t = ph
    p_b = ph

    output_height = h - kh + (2 * ph) + 1
    output_width = w - kw + (2 * pw) + 1

    output = np.zeros((m, output_height, output_width))

    image_padded = np.pad(
        images, ((0, 0), (p_t, p_b), (p_l, p_r)),
        mode="constant", constant_values=0)
    for h in range(output_height):
        for w in range(output_width):
            output[:, h, w] = np.sum(
                kernel * image_padded[:, h: h + kh, w: w + kw], axis=(1, 2))
    return output
