#!/usr/bin/env python3
"""
one hot
"""


import tensorflow.keras as Keras


def one_hot(labels, classes=None):
    """
    One hot encoder
    """
    return Keras.utils.to_categorical(labels, classes)
