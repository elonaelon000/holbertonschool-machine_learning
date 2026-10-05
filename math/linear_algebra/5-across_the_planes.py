#!/usr/bin/env python3
"""Module for adding two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Return a new matrix containing the element-wise sum of two matrices."""
    if len(mat1) != len(mat2):
        return None

    if any(len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)):
        return None

    return [
        [a + b for a, b in zip(row1, row2)]
        for row1, row2 in zip(mat1, mat2)
    ]
