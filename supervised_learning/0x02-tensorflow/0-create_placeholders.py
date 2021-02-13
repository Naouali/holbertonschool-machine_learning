#!/usr/bin/env python3
"""
placeholders in tensor flow
"""


import tensorflow as tf


def create_placeholders(nx, classes):
    """
    placeholders function
    """
    x = tf.placeholder(name="x", dtype=tf.float32, shape=(None, xn))
    y = tf.placeholder(name="y", dtype=tf.float32, shape=(None, classes))
    return x, y
