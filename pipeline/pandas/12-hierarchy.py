#!/usr/bin/env python3
"""Combine exchange data with timestamps as the outer index."""

import pandas as pd

index = __import__('10-index').index


def hierarchy(df1, df2):
    """Return both exchanges in chronological order for the given range."""
    df1 = index(df1)
    df2 = index(df2)
    start, end = 1417411980, 1417417980
    df1 = df1.loc[(df1.index >= start) & (df1.index <= end)]
    df2 = df2.loc[(df2.index >= start) & (df2.index <= end)]
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
    return df.swaplevel(0, 1).sort_index()
