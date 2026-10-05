#!/usr/bin/env python3
"""Module for adding matrices of arbitrary dimensions."""


def add_matrices(mat1, mat2):
    """Return the element-wise sum of two matrices of the same shape."""
    if len(mat1) != len(mat2):
        return None

    if isinstance(mat1[0], list) != isinstance(mat2[0], list):
        return None

    if not isinstance(mat1[0], list):
        return [a + b for a, b in zip(mat1, mat2)]

    result = []
    for sub1, sub2 in zip(mat1, mat2):
        added = add_matrices(sub1, sub2)
        if added is None:
            return None
        result.append(added)
    return result
