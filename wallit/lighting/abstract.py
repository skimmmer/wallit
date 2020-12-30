"""Color (RGB) LED lighting."""

from abc import ABC, abstractmethod


class Color:
    """RGB-based color."""
    def __init__(self, red, blue, green, white=None):
        self.red = red
        self.blue = blue
        self.green = green
        self.white = white

    def __str__(self):
        return f"#{self.red:x}{self.blue:x}{self.green:x}"

    def __eq__(self, other):
        v = other if isinstance(other, Color) else self.from_string(other)
        return self.red == v.red and self.blue == v.blue and self.green == v.green and self.white == v.white

    @classmethod
    def from_rgb(cls, red, blue, green):
        return cls(red, blue, green)

    @classmethod
    def from_rgbw(cls, red, blue, green, white=None):
        return cls(red, blue, green, white)

    @classmethod
    def from_hex(cls, hex_string):
        hex_string = hex_string.lstrip('#')
        if len(hex_string) == 3:
            hex_string = ''.join([c * 2 for c in hex_string])
        colors = [int(hex_string[c:c + 2], 16) for c in range(0, 6, 2)]
        return cls(*colors)

    @classmethod
    def from_string(cls, string):
        if string.startswith('#'):
            return cls.from_hex(string)
        elif ',' in string:
            return cls.from_rgbw(*string.split(','))
        raise ValueError('Invalid color format')

    @classmethod
    def blank(cls):
        return cls(0, 0, 0)


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