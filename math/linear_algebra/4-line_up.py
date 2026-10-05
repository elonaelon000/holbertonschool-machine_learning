#!/usr/bin/env python3
"""Module for adding two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Return a new list containing the element-wise sum of two arrays."""
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
