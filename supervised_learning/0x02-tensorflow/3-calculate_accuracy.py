#!/usr/bin/env python3
"""
calcualte accuracy
"""


import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    accuarcy function
    """

    return y-y_pred.tf.mean()
