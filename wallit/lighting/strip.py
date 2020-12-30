"""Strip lighting."""
from .abstract import Lighting
import rpi_ws281x


class StripLighting(Lighting):
    """Lighting based on WS281x."""
    LIGHTING_PIN = 18  # GPIO connect to lighting
    FREQUENCY = 800000  # Lighting signal frequency
    DMA_CHANNEL = 10  # DMA channel for PWM generation
    DEFAULT_BRIGHTNESS = 255  # Initial lighting brightness

    def __init__(self, pixels):
        self.strip = rpi_ws281x.PixelStrip(pixels, self.LIGHTING_PIN,
                                           self.FREQUENCY, self.DMA_CHANNEL,
                                           False, self.DEFAULT_BRIGHTNESS,
                                           0 if self.LIGHTING_PIN == 18 else 1)

        self.strip.begin()

    def set_pixel(self, index, color):
        self.strip.setPixelColorRGB(index, color.red, color.blue, color.green)

    def pixel(self, index):
        rgb = self.strip.getPixelColorRGB(index)
        return Color.from_rgb(rgb.r, rgb.b, rgb.g)

    def show(self):
        self.strip.show()