#!/usr/bin/env python3
"""
CNN
"""


import numpy as np


def conv_backward(dZ, A_prev, W, b, padding="same", stride=(1, 1)):
    """
    CNN
    """
    m, h_new, w_new, c_new = dZ.shape
    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, _, _ = W.shape
    sh, sw = stride
    h, w = h_new, w_new

    dA_prev = np.zeros(A_prev.shape)
    dW = np.zeros(W.shape)
    db = np.zeros(b.shape)

    if padding == "same":
        ph = int(((h - 1) * sh + kh - kh % 2 - h) / 2 + 1)
        pw = int(((w - 1) * sw + kw - kw % 2 - w) / 2 + 1)

    elif padding == "valid":
        ph, pw = 0, 0

    A_prev_pad = np.pad(
        A_prev, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        constant_values=0, mode='constant')
    dA_prev_pad = np.pad(
        dA_prev, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        constant_values=0, mode='constant')

    for i in range(m):
        a_prev_pad = A_prev_pad[i]
        da_prev_pad = dA_prev_pad[i]

        for h in range(h_new):
            for w in range(w_new):
                for c in range(c_new):
                    vs = h * sh
                    ve = h * sh + kh
                    hs = w * sw
                    he = w * sw + kw

                    a_slice = a_prev_pad[vs:ve, hs:he, :]

                    da_prev_pad[vs:ve, hs:he, :] += W[:,
                                                      :, :, c] * dZ[i, h, w, c]
                    dW[:, :, :, c] += a_slice * dZ[i, h, w, c]
                    db[:, :, :, c] += dZ[i, h, w, c]
        if (padding == 'valid'):
            dA_prev[i, :, :, :] = da_prev_pad
        elif (padding == 'same'):
            dA_prev[i, :, :, :] = da_prev_pad[ph:-ph, pw:-pw, :]
    return dA_prev, dW, db
