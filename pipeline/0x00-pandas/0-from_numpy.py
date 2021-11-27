#!/usr/bin/env python3
import pandas as pd


def from_numpy(array):
    """
    Create pandas dataFrame From numpy array
    """
    Columns = list(map(chr, range(65, 91)))
    print(list(Columns))
    df = pd.DataFrame(array)
    df.columns = Columns[:array.shape[1]]
    return df
