#!/usr/bin/env python3
"""Module for concatenating matrices along a specified axis."""


def _shape(matrix):
    """Return the shape of a nested list as a tuple."""
    if not isinstance(matrix, list):
        return ()
    return (len(matrix),) + _shape(matrix[0])


def _copy(matrix):
    """Return a deep copy of a nested list matrix."""
    if not isinstance(matrix, list):
        return matrix
    return [_copy(element) for element in matrix]


def cat_matrices(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis."""
    shape1 = _shape(mat1)
    shape2 = _shape(mat2)

    if len(shape1) != len(shape2) or axis >= len(shape1):
        return None

    if shape1[:axis] + shape1[axis + 1:] != \
            shape2[:axis] + shape2[axis + 1:]:
        return None

    if axis == 0:
        return _copy(mat1) + _copy(mat2)

    return [cat_matrices(a, b, axis - 1) for a, b in zip(mat1, mat2)]
