#!/usr/bin/env python3
"""Module for slicing NumPy arrays along specified axes."""


def np_slice(matrix, axes={}):
    """Return a new array sliced along the specified axes."""
    slices = [slice(None)] * matrix.ndim
    for axis, values in axes.items():
        slices[axis] = slice(*values)
    return matrix[tuple(slices)].copy()
