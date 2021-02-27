#!/usr/bin/env python3
"""
learning rate decay tensorflow
"""


import tensorflow as tf


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    wit tf
    """
    return tf.train.inverse_time_decay(
        alpha, global_step, decay_step, decay_rate, staircase=True)
