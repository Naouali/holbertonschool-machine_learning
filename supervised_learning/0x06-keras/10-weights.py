#!/usr/bin/env python3
"""
Model weights
"""


import tensorflow.keras as Keras


def save_weights(network, filename, save_format='h5'):
    """
    weight
    """
    network.save_weights(filename, save_format=save_format)
    return None


def load_weights(network, filename):
    """
    Load weights
    """
    network.load_weights(filename)
    return None
