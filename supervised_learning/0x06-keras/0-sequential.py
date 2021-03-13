#!/usr/bin/env python3
"""
Keras sequatial
"""


import tensorflow as tf
import tensorflow.keras as keras


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    build model
    """
    model = keras.Sequential()
    for i in range(1, len(layers)):
        model.add(keras.layers.Dropout(1 - keep_prob))
        model.add(keras.layers.Dense(
            layers[i],
            activations[i],
            input_shape=nx,
            kernel_regularizer=keras.regularizers.l2(lambtha),
        ))

    return model
