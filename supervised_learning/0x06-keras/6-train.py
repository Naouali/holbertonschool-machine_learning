#!/usr/bin/env python3
"""
Train
"""


import tensorflow.keras as Keras


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, verbose=True, shuffle=False):
    """
    Train
    """
    call = []
    if (early_stopping and validation_data):
        call = [Keras.call.EarlyStopping(
            monitor="val_loss", patience=patience)]
    else:
        call = None
    model = network.fit(
        data,
        labels,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=validation_data,
        shuffle=shuffle,
        verbose=verbose,
        callbacks=call)
    return model
