#!/usr/bin/env python3
"""
l2 regularization
"""


import tensorflow as tf


def l2_reg_cost(cost):
    """
    L2 regularization
    """
    reg = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
    l = cost + reg
    return l
