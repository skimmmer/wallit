"""Lighting mapping from one space to another."""
from .abstract import Lighting2D
import numpy as np


class LightingAs2D(Lighting2D):
    """Interpretation of Lighting as 2D through mapping."""
    def __init__(self, lighting, width, height):
        self.lighting = lighting
        self.width = width
        self.height = height
        self._mapping = np.ndarray((height, width),
                                   dtype=int,
                                   buffer=np.arange(width * height))

    def _point_as_index(self, x, y):
        return self._mapping[y][x]

    def set_pixel(self, x, y, color):
        self.lighting.set_pixel(self._point_as_index(x, y), color)

    def pixel(self, x, y):
        return self.lighting.pixel(self._point_as_index(x, y))

    def show(self):
        self.lighting.show()