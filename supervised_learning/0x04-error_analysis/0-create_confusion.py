#!/usr/bin/env python3
"""
COnfusion matrix
"""


import numpy as np


def create_confusion_matrix(labels, logits):
    """
    confuion matrix
    """
    classes = logits.shape[1]
    m = logits.shape[0]
    conf = np.zeros((classes, classes))
    for i in range(m):
        conf[np.where(labels[i, :] == 1), np.where(logits[i, :] == 1)] += 1
    return conf
