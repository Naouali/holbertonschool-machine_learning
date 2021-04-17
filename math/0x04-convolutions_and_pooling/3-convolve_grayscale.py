#!/usr/bin/env python3
"""
Convolve
"""


import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a same convolution on grayscale images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride
    if padding == "same":
        output_height = h
        output_width = w

        pad_h = int(np.ceil(((h - 1) * sh + kh - h) / 2))
        pad_w = int(np.ceil(((w - 1) * sw + kw - w) / 2))

        image_padded = np.zeros((m, h + 2 * pad_h, w + 2 * pad_w))
        image_padded[:, pad_h:h + pad_h, pad_w:w + pad_w] = np.copy(images)
    elif padding == "valid":
        output_height = int(np.ceil((h - kh + 1) / sh))
        output_width = int(np.ceil((w - kw + 1) / sw))
        image_padded = np.copy(images)

    elif isinstance(padding, tuple):
        ph, pw = padding
        p_l = pw
        p_r = pw
        p_t = ph
        p_b = ph

        output_height = int((h - kh + (2 * ph) + 1) // sh)
        output_width = int((w - kw + (2 * pw) + 1) // sw)

        image_padded = np.pad(
            images, ((0, 0), (p_t, p_b), (p_l, p_r)),
            mode="constant", constant_values=0)

    output = np.zeros((m, output_height, output_width))
    for h in range(output_height):
        for w in range(output_width):
            h_s = h * sh
            w_s = w * sw
            output[:, h, w] = np.sum(
                image_padded[:, h_s: h_s + kh, w_s: w_s + kw] * kernel,
                axis=(1, 2))
    return output
