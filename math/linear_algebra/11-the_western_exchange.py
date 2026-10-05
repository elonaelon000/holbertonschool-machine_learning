#!/usr/bin/env python3
"""Module for transposing NumPy arrays."""


def np_transpose(matrix):
    """Return a new NumPy array containing the transpose of matrix."""
    return matrix.T.copy()
