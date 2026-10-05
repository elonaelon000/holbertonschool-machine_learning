#!/usr/bin/env python3
"""Module for NumPy element-wise arithmetic."""

import numpy as np


def np_elementwise(mat1, mat2):
    """Return element-wise sum, difference, product, and quotient."""
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
