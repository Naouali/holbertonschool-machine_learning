#!/usr/bin/env python3
"""
calcualte accuracy
"""


import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    accuarcy function
    """
    eq = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))
    acc = tf.reduce_mean(tf.cast(eq, tf.float32))
    return acc
