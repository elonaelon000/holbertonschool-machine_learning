#!/usr/bin/env python3
"""Select price and volume columns at sixty-row intervals."""


def slice(df):
    """Return every sixtieth row of High, Low, Close, and Volume_(BTC)."""
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
