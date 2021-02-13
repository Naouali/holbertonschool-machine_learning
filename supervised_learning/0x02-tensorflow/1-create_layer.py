#!/usr/bin/env python3
"""
create layer
"""


import tensorflow as tf


def create_layer(prev, n, activation):
    """
    create layer function
    """
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")

    model = tf.layers.Dense(units=n,
                            activation=activation,
                            kernel_initializer=init)
    return model(prev)
