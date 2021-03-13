#!/usr/bin/env python3
"""
Input
"""


import tensorflow.keras as Keras


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Input
    """
    inputs = Keras.Input(shape=(nx,))
    l2 = kernel_regularizer = Keras.regularizers.l2(lambtha)
    dense = Keras.layers.Dense(
        layers[0],
        activation=activations[0],
        kernel_regularizer=l2)
    x = dense(inputs)
    for i in range(1, len(layers)):
        x = Keras.layers.Dropout(1 - keep_prob)(x)
        x = Keras.layers.Dense(
            layers[i],
            activation=activations[i],
            kernel_regularizer=l2)(x)

    model = Keras.Model(inputs=inputs, outputs=x)
    return model
