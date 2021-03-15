#!/usr/bin/env python3
"""
Deep CNN
"""

import tensorflow.keras as K


def transition_layer(X, filters, compression):
    """
    Transition layer
    """
    init = K.initializers.he_normal(seed=None)

    Layer = K.layers.BatchNormalization()(X)
    Layer = K.layers.Activation('relu')(Layer)

    filters = int(filters * compression)

    Layer = K.layers.Conv2D(filters=filters,
                               kernel_size=1,
                               padding='same',
                               kernel_initializer=init,
                               )(Layer)

    X = K.layers.AveragePooling2D(pool_size=2,
                                  padding='same')(Layer)

    return X, filters

