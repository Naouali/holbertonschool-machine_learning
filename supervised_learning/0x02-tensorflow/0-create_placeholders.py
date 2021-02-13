#!/usr/bin/env python3
"""
placeholders in tensor flow
"""


import tensorflow as tf


def create_placeholders(nx, classes):
    """
    placeholders function
    """
    x = tf.placeholder(dtype=tf.float32, shape=(None, xn), name="x")
    y = tf.placeholder(dtype=tf.float32, shape=(None, classes), name="y")
    return x, y
