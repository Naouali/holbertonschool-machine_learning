#!/usr/bin/env python3
"""
Deep CNN
"""


import tensorflow.keras as keras
inception_block = __import__('0-inception_block').inception_block


def inception_network():
    """
    Builds the inception network
    """
    init = keras.initializers.he_normal(seed=None)

    X = keras.Input(shape=(224, 224, 3))

    Layer = keras.layers.Conv2D(filters=64,
                               kernel_size=(7, 7),
                               strides=(2, 2),
                               padding='same',
                               activation='relu',
                               kernel_initializer=init,
                               )(X)

    Layer = keras.layers.MaxPool2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(2, 2)
                                  )(Layer)

    Layer = keras.layers.Conv2D(filters=64,
                               kernel_size=(1, 1),
                               strides=(1, 1),
                               padding='same',
                               activation='relu',
                               kernel_initializer=init,
                               )(Layer)

    Layer = keras.layers.Conv2D(filters=192,
                               kernel_size=(3, 3),
                               strides=(1, 1),
                               padding='same',
                               activation='relu',
                               kernel_initializer=init,
                               )(Layer)

    Layer = keras.layers.MaxPool2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(2, 2)
                                  )(Layer)

    Layer = inception_block(Layer, [64, 96, 128, 16, 32, 32])

    Layer = inception_block(Layer, [128, 128, 192, 32, 96, 64])

    Layer = keras.layers.MaxPool2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(2, 2)
                                  )(Layer)

    Layer = inception_block(Layer, [192, 96, 208, 16, 48, 64])
    Layer = inception_block(Layer, [160, 112, 224, 24, 64, 64])
    Layer = inception_block(Layer, [128, 128, 256, 24, 64, 64])
    Layer = inception_block(Layer, [112, 144, 288, 32, 64, 64])
    Layer = inception_block(Layer, [256, 160, 320, 32, 128, 128])

    Layer = keras.layers.MaxPool2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(2, 2)
                                  )(Layer)

    Layer = inception_block(Layer, [256, 160, 320, 32, 128, 128])
    Layer = inception_block(Layer, [384, 192, 384, 48, 128, 128])

    Layer = keras.layers.AveragePooling2D(pool_size=(7, 7),
                                         padding='same'
                                         )(Layer)

    Layer = keras.layers.Dropout(rate=0.4)(Layer)

    Layer = keras.layers.Dense(units=1000,
                              activation='softmax',
                              kernel_initializer=init,
                              )(Layer)

    model = keras.models.Model(inputs=X, outputs=Layer)

    return model
