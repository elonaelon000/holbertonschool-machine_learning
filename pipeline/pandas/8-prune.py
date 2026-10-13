#!/usr/bin/env python3
"""Remove rows with missing Close prices."""


def prune(df):
    """Return the DataFrame without rows where Close is missing."""
    return df.dropna(subset=['Close'])
