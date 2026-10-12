#!/usr/bin/env python3
"""Rename and convert a DataFrame's timestamp column."""

import pandas as pd


def rename(df):
    """Return the Datetime and Close columns with timestamps converted."""
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    return df[['Datetime', 'Close']]
