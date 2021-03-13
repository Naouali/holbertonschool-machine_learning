#!/usr/bin/env python3
"""
lenet5
"""


import tensorflow.keras as Keras


def lenet5(X):
    """
    lenet5
    """
    w = K.initializers.he_normal(seed=None)
    conv = K.layers.Conv2D(filters=6, kernel_size=5,
                           padding='same', activation='relu',
                           kernel_initializer=w)(X)
    pool = K.layers.MaxPooling2D(pool_size=2, strides=(2, 2))(conv)
    conv = K.layers.Conv2D(filters=16, kernel_size=5,
                           padding='valid', activation='relu',
                           kernel_initializer=w)(pool)
    pool = K.layers.MaxPooling2D(pool_size=2, strides=2)(conv)
    flat = K.layers.Flatten()(pool)
    n = K.layers.Dense(units=120, activation='relu',
                       kernel_initializer=w)(flat)
    n = K.layers.Dense(units=84, activation='relu',
                       kernel_initializer=w)(n)
    n = K.layers.Dense(units=10, activation='softmax',
                       kernel_initializer=w)(n)
    model = K.models.Model(inputs=X, outputs=n)
    model.compile(loss='categorical_crossentropy',
                  optimizer=K.optimizers.Adam(),
                  metrics=['accuracy'])
    return model
