#!/usr/bin/env python3
"""
CNN
"""


import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    """
    CNN
    """
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, c_prev, c_new = W.shape
    sh, sw = stride

    p_h = 0
    p_w = 0

    if padding == "same":
        p_h = int(np.ceil((sh * (h_prev - 1) - h_prev + kh) / 2))
        p_w = int(np.ceil((sw * (w_prev - 1) - w_prev + kw) / 2))

    A_padded = np.pad(
        array=A_prev,
        pad_width=((0,), (p_h,), (p_w,), (0,)),
        mode="constant",
        constant_values=0
    )
    output_h = int((h_prev + 2 * p_h - kh) / sh + 1)
    output_w = int((w_prev + 2 * p_w - kw) / sw + 1)

    output = np.zeros((m, output_h, output_w, c_new))

    for i in range(output_h):
        for j in range(output_w):
            for k in range(c_new):
                output[:, i, j, k] = np.sum(
                    W[:, :, :, k] *
                    A_padded[:, i * sh:i * sh + kh, j * sw:j * sw + kw],
                    axis=(1, 2, 3)
                )
    return activation(output + b)
