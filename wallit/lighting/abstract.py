"""Color (RGB) LED lighting."""

from abc import ABC, abstractmethod


class Color:
    """RGB-based color."""
    def __init__(self, red, blue, green, white=None):
        self.red = red
        self.blue = blue
        self.green = green
        self.white = white

    @classmethod
    def from_rgb(cls, red, blue, green):
        return cls(red, blue, green)

    @classmethod
    def from_rgb(cls, red, blue, green, white):
        return cls(red, blue, green, white)


class Lighting(ABC):
    """Lighting definition by pixel index."""
    @abstractmethod
    def set_pixel(self, index, color):
        """Set pixel color by index."""
        raise NotImplementedError

    def set_pixels(self, pixels):
        """Set pixel colors."""
        for i, row in enumerate(pixels):
            self.set_pixel(i, color)

    @abstractmethod
    def pixel(self, index):
        """Get pixel color at index."""
        raise NotImplementedError

    @abstractmethod
    def show(self):
        """Display buffered lighting settings."""
        raise NotImplementedError


class Lighting2D(ABC):
    """2D Lighting definition by x/y."""
    @abstractmethod
    def set_pixel(self, x, y, color):
        """Set pixel color by x/y."""
        raise NotImplementedError

    def set_pixels(self, pixels):
        """Set pixel colors."""
        for x, row in enumerate(pixels):
            for y, color in enumerate(pixels):
                self.set_pixel(x, y, color)

    @abstractmethod
    def pixel(self, index):
        """Get pixel color at index."""
        raise NotImplementedError

    @abstractmethod
    def show(self):
        """Display buffered lighting settings."""
        raise NotImplementedError