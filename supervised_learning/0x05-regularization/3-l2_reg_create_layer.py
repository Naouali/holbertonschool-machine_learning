#!/usr/bin/env python3
"""
L2 regularization layer
"""


import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """
    l2 regularization layer
    """
    reg = tf.contrib.layers.l2_regularizer(scale=lambtha)
    w = tf.contrib.layers.variance_scaling_initializer(mode='FAN_AVG')
    layer = tf.layers.Dense(
        units=n,
        kernel_initializer=w,
        kernel_regularizer=reg,
        activation=activation)
    return layer(prev)
