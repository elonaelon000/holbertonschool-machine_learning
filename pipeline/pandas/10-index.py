#!/usr/bin/env python3
"""Use timestamps as DataFrame row labels."""


def index(df):
    """Return the DataFrame with Timestamp as its index."""
    return df.set_index('Timestamp')
