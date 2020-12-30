"""Wall description."""
import json as jsonlib
import numpy as np
from .lighting.abstract import Color


def verify_pixel(func):
    def verify_and_do(wall, x, y, *args, **kwargs):
        if not self.lighting:
            raise ValueError('Lighting not defined for wall')
        elif x >= self.width or x < 0:
            raise IndexError('x value outside of wall bounds')
        elif y >= self.height or y < 0:
            raise IndexError('y value outside of wall bounds')

        func(wall, x, y, *args, **kwargs)

    return verify_and_do


def verify_matrix(func):
    def verify_and_do(wall, matrix, *args, **kwargs):
        if not self.lighting:
            raise ValueError('Lighting not defined for wall')
        elif matrix.shape[1] > self.width:
            raise ValueError('matrix width outside of wall bounds')
        elif matrix.shape[0] > self.height:
            raise ValueError('matrix height outside of wall bounds')

        func(wall, x, y, *args, **kwargs)

    return verify_and_do


class Wall:
    def __init__(self, name, width, height, climbers=None):
        self.name = name
        self.width = width
        self.height = height
        self.climbers = climbers or []
        self.lighting = None

    def to_dict(self):
        return {
            'name': self.name,
            'climbers': self.climbers,
            'width': self.width,
            'height': self.height,
        }

    @verify_pixel
    def set_pixel(self, x, y, color):
        self.lighting.set_pixel(x, y, color)

    @verify_pixel
    def clear_pixel(self, x, y, color):
        self.lighting.set_pixel(x, y, Color.blank())

    @verify_pixel
    def pixel(self, x, y):
        return self.lighting.pixel(x, y, color)

    @verify_matrix
    def set_pixels(self, matrix):
        for y in range(self.height):
            for x in range(self.width):
                self.lighting.set_pixel(x, y, matrix[y][x])

    def clear_pixels(self, matrix):
        for y in range(self.height):
            for x in range(self.width):
                self.lighting.set_pixel(x, y, Color.blank())

    def pixels(self):
        if not self.lighting:
            raise ValueError('Lighting not defined for wall')
        matrix = np.ndarray((self.height, self.width), dtype='object')
        for y in range(self.height):
            for x in range(self.width):
                matrix[y][x] = self.lighting.pixel(x, y)
        return matrix

    @classmethod
    def from_json(cls, filename):
        with open(filename, 'r') as f:
            json = jsonlib.load(f)

        return cls(json['name'],
                   json['size']['width'],
                   json['size']['height'],
                   climbers=json.get('climbers'))