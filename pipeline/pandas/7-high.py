#!/usr/bin/env python3
"""Sort a DataFrame by the High column."""


def high(df):
    """Return rows sorted by High from largest to smallest."""
    return df.sort_values(by='High', ascending=False)
