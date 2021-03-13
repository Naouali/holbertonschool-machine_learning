#!/usr/bin/env python3
"""
test
"""


import tensorflow.keras as Keras


def test_model(network, data, labels, verbose=True):
    """
    tests model
    """
    return network.evaluate(data, labels, verbose=verbose)
