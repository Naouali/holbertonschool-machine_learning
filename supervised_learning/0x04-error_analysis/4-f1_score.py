#!/usr/bin/env python3
"""
f1 score
"""


sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """
    F1 score
    """
    ppv = precision(confusion)
    tpr = sensitivity(confusion)
    return 2 * ppv * tpr / (ppv + tpr)
