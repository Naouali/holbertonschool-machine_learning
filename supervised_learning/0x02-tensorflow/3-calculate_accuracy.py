#!/usr/bin/env python3
"""
calcualte accuracy
"""


import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    accuarcy function
    """

    return tf.reduce_mean(tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1)))

