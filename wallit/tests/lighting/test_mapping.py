from ...lighting.mapping import LightingAs2D
from unittest.mock import MagicMock

class TestMapping:
    def test_initial(self):
        mock = MagicMock()
        lighting = LightingAs2D(mock, 3, 4)
        lighting.set_pixel(2, 1, None)
        mock.set_pixel.assert_called_with(5, None)