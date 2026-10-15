#!/usr/bin/env python3
"""Plot sampled mountain elevations as a colored scatter plot."""

import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """Show elevation of sampled points on a mountain."""
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))

    plt.scatter(x, y, c=z, cmap='viridis')
    plt.xlabel('x coordinate (m)')
    plt.ylabel('y coordinate (m)')
    plt.title('Mountain Elevation')
    plt.colorbar(label='elevation (m)')
    plt.show()
