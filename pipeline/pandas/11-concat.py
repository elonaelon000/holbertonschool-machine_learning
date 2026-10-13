#!/usr/bin/env python3
"""Combine Bitstamp and Coinbase data with source labels."""

import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """Prepend Bitstamp rows through timestamp 1417411920 to Coinbase."""
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.loc[df2.index <= 1417411920]
    return pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
