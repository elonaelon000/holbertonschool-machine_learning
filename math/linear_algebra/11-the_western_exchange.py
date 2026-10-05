#!/usr/bin/env python3
"""Module for transposing NumPy arrays."""

import numpy as np


def np_transpose(matrix):
    """Return a new NumPy array containing the transpose of matrix."""
    return np.array(matrix).T.copy()
