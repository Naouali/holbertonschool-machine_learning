#!/usr/bin/env python3
'''
POOL
'''


import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs pooling on images
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    output_h = int((h - kh) / sh + 1)
    output_w = int((w - kw) / sw + 1)

    output = np.zeros((m, output_h, output_w, c))
    for h in range(output_h):
        for w in range(output_w):
            if mode == 'max':
                output[:, h, w, :] = np.max(
                    images[:, h * sh: h * sh + kh, w * sw: w * sw + kw, :],
                    axis=(1, 2))
            else:
                output[:, h, w, :] = np.mean(
                    images[:, h * sh: h * sh + kh, w * sw: w * sw + kw, :],
                    axis=(1, 2))
    return output
