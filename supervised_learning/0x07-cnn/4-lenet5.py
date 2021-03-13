#!/usr/bin/env python3
"""
lenet5
"""


import tensorflow as tf


def lenet5(x, y):
    """
    lenet5
    """
    W = tf.contrib.layers.variance_scaling_initializer()
    C1 = tf.layers.Conv2D(
        filters=6,
        kernel_size=(
            5,
            5),
        padding="same",
        activation='relu',
        kernel_initializer=W)(x)
    S2 = tf.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(C1)
    C3 = tf.layers.Conv2D(
        filters=16,
        kernel_size=(
            5,
            5),
        activation='relu',
        padding="valid",
        kernel_initializer=w)(S2)
    S4 = tf.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2))(C3)
    C5 = tf.layers.Flatten()(S4)
    F6 = tf.layers.Dense(
        units=120,
        activation='relu',
        kernel_initializer=w)(C5)
    F7 = tf.layers.Dense(units=84, activation='relu', kernel_initializer=w)(F6)
    F8 = tf.layers.Dense(units=10, kernel_initializer=w)(F7)

    s = tf.nn.softmax(F8)

    loss = tf.losses.softmax_cross_entropy(y, F8)

    equality = tf.equal(tf.argmax(F8, 1), tf.argmax(y, 1))
    acc = tf.reduce_mean(tf.cast(equality, tf.float32))
    adam = tf.train.AdamOptimizer().minimize(loss)
    return s, adam, loss, acc
