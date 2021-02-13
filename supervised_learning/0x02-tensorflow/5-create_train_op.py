#!/usr/bin/env python3
"""
train
"""


import tensorflow as tf


def create_train_op(loss, alpha):
    """
    train op
    """
    return tf.GradientDescentOptimizer(alpha).minimize(loss)
