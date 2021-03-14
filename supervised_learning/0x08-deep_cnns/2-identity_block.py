#!/usr/bin/env python3
"""
Deep cnn
"""


import tensorflow.keras as K


def identity_block(A_prev, filters):
    """
    identity block
    """
    F11, F3, F12 = filters
    init = K.initializers.he_normal(seed=None)
    Layer = K.layers.Conv2D(filters=F11,
                               kernel_size=(1, 1),
                               padding='same',
                               kernel_initializer=init,
                               )(A_prev)

    Layer = K.layers.BatchNormalization(axis=3)(Layer)
    Layer = K.layers.Activation('relu')(Layer)
    Layer = K.layers.Conv2D(filters=F3,
                               kernel_size=(3, 3),
                               padding='same',
                               kernel_initializer=init,
                               )(Layer)

    Layer = K.layers.BatchNormalization(axis=3)(Layer)
    Layer = K.layers.Activation('relu')(Layer)
    Layer = K.layers.Conv2D(filters=F12,
                               kernel_size=(1, 1),
                               padding='same',
                               kernel_initializer=init,
                               )(Layer)

    Layer = K.layers.BatchNormalization(axis=3)(Layer)
    output = K.layers.Add()([Layer, A_prev])
    output = K.layers.Activation('relu')(output)

    return output
