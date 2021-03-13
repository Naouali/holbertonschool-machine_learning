#!/usr/bin/env python3
"""
Predict
"""


import tensorflow.keras as Keras


def predict(network, data, verbose=False):
    """
    model
    """
    return network.predict(data, verbose=verbose)
