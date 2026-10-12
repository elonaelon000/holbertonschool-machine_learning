#!/usr/bin/env python3
"""Load a pandas DataFrame from a file."""

import pandas as pd


def from_file(filename, delimiter):
    """Read a file using the given column separator."""
    return pd.read_csv(filename, sep=delimiter)
