#!/usr/bin/env python3
"""
Deep CNN
"""


import tensorflow.keras as Keras


def inception_block(A_prev, filters):
    """
    Deep CNN
    """
    F1, F3R, F3, F5R, F5, FPP = filters
    init = Keras.initializers.he_normal(seed=None)

    layer = Keras.layers.Conv2D(filters=F1,
                                   kernel_size=(1, 1),
                                   padding='same',
                                   activation='relu',
                                   kernel_initializer=init,
                                   )(A_prev)

    layer1 = Keras.layers.Conv2D(filters=F3R,
                                    kernel_size=(1, 1),
                                    padding='same',
                                    activation='relu',
                                    kernel_initializer=init,
                                    )(A_prev)

    layer1 = Keras.layers.Conv2D(filters=F3,
                                    kernel_size=(3, 3),
                                    padding='same',
                                    activation='relu',
                                    kernel_initializer=init,
                                    )(layer1)

    layer2 = Keras.layers.Conv2D(filters=F5R,
                                    kernel_size=(1, 1),
                                    padding='same',
                                    activation='relu',
                                    kernel_initializer=init,
                                    )(A_prev)

    layer2 = Keras.layers.Conv2D(filters=F5,
                                    kernel_size=(5, 5),
                                    padding='same',
                                    activation='relu',
                                    kernel_initializer=init,
                                    )(layer2)

    layer3 = Keras.layers.MaxPool2D(pool_size=(3, 3),
                                       padding='same',
                                       strides=(1, 1)
                                       )(A_prev)

    layer3 = Keras.layers.Conv2D(filters=FPP,
                                kernel_size=(1, 1),
                                padding='same',
                                activation='relu',
                                kernel_initializer=init,
                                    )(layer3)

    output = Keras.layers.concatenate([layer, layer1,
                                      layer2, layer3])

    return output
