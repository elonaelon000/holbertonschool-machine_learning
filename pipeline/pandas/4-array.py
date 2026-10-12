#!/usr/bin/env python3
"""Extract DataFrame values as a NumPy array."""


def array(df):
    """Return High and Close values from the last ten rows."""
    return df[['High', 'Close']].tail(10).values
