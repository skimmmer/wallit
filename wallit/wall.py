"""Wall description."""
import json as jsonlib


class Wall:
    def __init__(self, name, width, height, climbers=None):
        self.name = name
        self.width = width
        self.height = height
        self.climbers = climbers or []

    def to_dict(self):
        return {
            'name': self.name,
            'climbers': self.climbers,
            'width': self.width,
            'height': self.height,
        }

    @classmethod
    def from_json(cls, filename):
        with open(filename, 'r') as f:
            json = jsonlib.load(f)

        return cls(json['name'],
                   json['size']['width'],
                   json['size']['height'],
                   climbers=json.get('climbers'))