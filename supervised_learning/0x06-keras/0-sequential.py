#!/usr/bin/env python3
"""
Build model
"""


import tensorflow.keras as Keras


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Build model
    """
    model = Keras.Sequential()
    l2 = Keras.regularizers.l2(lambtha)
    model.add(Keras.layers.Dense(
        layers[0],
        activation=activations[0],
        input_shape=(nx,),
        kernel_regularizer=l2))

    for i in range(1, len(layers)):
        model.add(Keras.layers.Dropout(1 - keep_prob))
        model.add(
            Keras.layers.Dense(
                layers[i],
                activation=activations[i],
                kernel_regularizer=l2))
    return model
