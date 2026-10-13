#!/usr/bin/env python3
"""Compute descriptive statistics for price and volume data."""


def analyze(df):
    """Return summary statistics for all columns except Timestamp."""
    return df.drop(columns=['Timestamp']).describe()
