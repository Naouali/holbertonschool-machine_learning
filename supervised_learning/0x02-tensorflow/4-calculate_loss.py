#!/usr/bin/env python3
"""
loss
"""


import tensorflow as tf


def calculate_loss(y, y_pred):
    """
    calculate loss function
    """

    return tf.losses.softmax_cross_entropy(y, y_pred)
