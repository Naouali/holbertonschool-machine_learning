#!/usr/bin/env python3
"""
Deep CNN
"""


import tensorflow.keras as K
identity_block = __import__('2-identity_block').identity_block
projection_block = __import__('3-projection_block').projection_block


def resnet50():
    """
    Rsent algo
    """
    init = K.initializers.he_normal(seed=None)

    X = K.Input(shape=(224, 224, 3))

    Layer = K.layers.Conv2D(filters=64,
                               kernel_size=(7, 7),
                               strides=(2, 2),
                               padding='same',
                               kernel_initializer=init,
                               )(X)

    Layer = K.layers.BatchNormalization(axis=3)(Layer)
    Layer = K.layers.Activation('relu')(Layer)

    Layer = K.layers.MaxPool2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(2, 2))(Layer)

    Layer = projection_block(Layer, [64, 64, 256], 1)
    for i in range(2):
        Layer = identity_block(Layer, [64, 64, 256])

    Layer = projection_block(Layer, [128, 128, 512])
    for i in range(3):
        Layer = identity_block(Layer, [128, 128, 512])

    Layer = projection_block(Layer, [256, 256, 1024])
    for i in range(5):
        Layer = identity_block(Layer, [256, 256, 1024])

    Layer = projection_block(Layer, [512, 512, 2048])
    for i in range(2):
        Layer = identity_block(Layer, [512, 512, 2048])

    Layer = K.layers.AveragePooling2D(pool_size=(7, 7),
                                         padding='same')(Layer)

    Layer = K.layers.Dense(units=1000,
                              activation='softmax',
                              kernel_initializer=init,
                              )(Layer)

    model = K.models.Model(inputs=X, outputs=Layer)

    return model
