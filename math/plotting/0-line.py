#!/usr/bin/env python3
"""Draw a line graph with Matplotlib."""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plot the cubes of numbers from 0 to 10 as a solid red line."""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(y, color='red', linestyle='-')
    plt.xlim(0, 10)
    plt.show()
