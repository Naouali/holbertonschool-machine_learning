#!/usr/bin/env python3
"""
Train
"""


import tensorflow.keras as Keras


def train_model(network, data, labels, batch_size,
                epochs, verbose=True, shuffle=False):
    """
    Train
    """
    fit = network.fit(data, labels, batch_size=batch_size,
                      epochs=epochs, shuffle=shuffle, verbose=verbose)
    return fit
