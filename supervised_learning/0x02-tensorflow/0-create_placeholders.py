#!/usr/bin/env python3
"""
placeholders in tensor flow
"""


import tensorflow as tf



def create_placeholders(nx, classes):
    """
    placeholders function
    """
    x =tf.placeholder(tf.float32, (, xn), name="x")
    y =tf.placeholder(tf.float32, (, classes), name="y")
    return x, y

