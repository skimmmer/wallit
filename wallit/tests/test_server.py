from .. import server
from pytest import fixture
from flask import json, jsonify
from unittest.mock import MagicMock


@fixture()
def client():
    server.current_wall = MagicMock()
    server.current_wall.to_dict.return_value = {
        'name': 'some wall',
        'width': 64,
        'height': 96
    }
    with server.app.test_client() as client:
        yield client


def test_wall(client):
    resp = client.get('/wall')
    data = json.loads(resp.data)
    assert data['name'] == 'some wall'
    assert data['width'] == 64
    assert data['height'] == 96