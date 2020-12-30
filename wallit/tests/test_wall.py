from ..wall import Wall

class TestWall:
    def test_from_json(self):
        wall = Wall.from_json("wallit/tests/fixtures/basic_wall.json")
        assert wall.name == 'basic wall'
        assert wall.width == 64
        assert wall.height == 96
        assert wall.climbers == ["joe_cool"]