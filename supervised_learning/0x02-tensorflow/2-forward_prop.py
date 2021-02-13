#!/usr/bin/env python3
"""
forward prop
"""


import tensorflow as tf
create_layer = __import__('0-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    for nodes, acts in zip(layer_sizes, activations):
        y = create_layer(x, nodes, acts)
        x = y
    return y
