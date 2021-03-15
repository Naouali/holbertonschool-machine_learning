#!/usr/bin/env python3
"""
Depp CNN
"""

import tensorflow.keras as K


def projection_block(A_prev, filters, s=2):
    """
    projection block
    """
    F11, F3, F12 = filters

    init = K.initializers.he_normal(seed=None)

    Layer = K.layers.Conv2D(filters=F11,
                               kernel_size=(1, 1),
                               strides=(s, s),
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

    short_c = K.layers.Conv2D(filters=F12,
                              kernel_size=(1, 1),
                              strides=(s, s),
                              padding='same',
                              kernel_initializer=init,
                              )(A_prev)

    short_c = K.layers.BatchNormalization(axis=3)(short_c)

    output = K.layers.Add()([Layer, short_c])

    output = K.layers.Activation('relu')(output)

    return output

