#!/usr/bin/env python3
"""Sort and transpose a DataFrame."""


def flip_switch(df):
    """Sort rows by descending index, then transpose the DataFrame."""
    return df.sort_index(ascending=False).T
