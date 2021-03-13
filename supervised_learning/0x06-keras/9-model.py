#!/usr/bin/env python3
"""
MODEL
"""


import tensorflow.keras as Keras


def save_model(network, filename):
    """
    Save model
    """
    network.save(filename)
    return None


def load_model(filename):
    """
    Load model
    """
    model = Keras.models.load_model(filename)
    return model
