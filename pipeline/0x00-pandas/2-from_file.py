#!/usr/bin/env python3
"""
Create DataFrame form file
"""

import pandas as pd


def from_file(filename, delimiter):
    """
    @filename: file to be readed
    @Dilimiter: dilimiter of the columns
    """
    df = pd.read_csv(filename, delimiter=delimiter)
    return df