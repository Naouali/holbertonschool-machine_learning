#!/usr/bin/env python3
"""
Deep CNN
"""


import tensorflow.keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    """
    Dense block
    """
    init = K.initializers.he_normal(seed=None)

    for i in range(layers):
        Layer = K.layers.BatchNormalization()(X)
        Layer = K.layers.Activation('relu')(Layer)

        Layer = K.layers.Conv2D(filters=4*growth_rate,
                                   kernel_size=1,
                                   padding='same',
                                   kernel_initializer=init,
                                   )(Layer)

        Layer = K.layers.BatchNormalization()(Layer)
        Layer = K.layers.Activation('relu')(Layer)

        Layer = K.layers.Conv2D(filters=growth_rate,
                                   kernel_size=3,
                                   padding='same',
                                   kernel_initializer=init,
                                   )(Layer)

        X = K.layers.concatenate([X, Layer])
        nb_filters += growth_rate

    return X, nb_filters
