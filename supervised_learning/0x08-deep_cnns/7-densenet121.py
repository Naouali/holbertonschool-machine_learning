#!/usr/bin/env python3
"""
Deep CNN
"""

import tensorflow.keras as K
dense_block = __import__('5-dense_block').dense_block
transition_layer = __import__('6-transition_layer').transition_layer


def densenet121(growth_rate=32, compression=1.0):
    """
    DenseNet-121
    """
    init = K.initializers.he_normal(seed=None)

    X = K.Input(shape=(224, 224, 3))
    layers = [12, 24, 16]

    Layer = K.layers.BatchNormalization(axis=3)(X)
    Layer = K.layers.Activation('relu')(Layer)

    Layer = K.layers.Conv2D(filters=2 * growth_rate,
                               kernel_size=(7, 7),
                               strides=(2, 2),
                               padding='same',
                               kernel_initializer=init,
                               )(Layer)

    Layer = K.layers.MaxPool2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(2, 2))(Layer)

    nb_filters = 2 * growth_rate

    Layer, nb_filters = dense_block(Layer, nb_filters, growth_rate, 6)

    for layer in layers:
        Layer, nb_filters = transition_layer(Layer,
                                                nb_filters,
                                                compression)

        Layer, nb_filters = dense_block(Layer,
                                           nb_filters,
                                           growth_rate,
                                           layer)

    Layer = K.layers.AveragePooling2D(pool_size=(7, 7),
                                         padding='same')(Layer)

    Layer = K.layers.Dense(units=1000,
                              activation='softmax',
                              kernel_initializer=init,
                              )(Layer)

    model = K.models.Model(inputs=X, outputs=Layer)
    return model

