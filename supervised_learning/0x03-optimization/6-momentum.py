#!/usr/bin/env python3
"""
upgraded
"""


import tensorflow as tf


def create_momentum_op(loss, alpha, beta1):
    """
    upgrade
    """
    return tf.train.MomentumOptimizer(alpha, beta1).minimize(loss)
