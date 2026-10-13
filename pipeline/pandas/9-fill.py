#!/usr/bin/env python3
"""Fill missing price and volume data."""


def fill(df):
    """Remove Weighted_Price and fill missing prices and volumes."""
    df = df.drop(columns=['Weighted_Price'])
    df['Close'] = df['Close'].ffill()
    for column in ['High', 'Low', 'Open']:
        df[column] = df[column].fillna(df['Close'])
    for column in ['Volume_(BTC)', 'Volume_(Currency)']:
        df[column] = df[column].fillna(0)
    return df
