#!/usr/bin/env python3
"""
Optimize
"""


import tensorflow.keras as Keras


def optimize_model(network, alpha, beta1, beta2):
    """
    optimizes
    """
    optimizer = Keras.optimizers.Adam(lr=alpha, beta_1=beta1, beta_2=beta2)

    network.compile(
        optimizer=optimizer,
        loss="categorical_crossentropy",
        metrics=['accuracy'])
    return None
