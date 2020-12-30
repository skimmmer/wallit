from .. import server
from pytest import fixture
from flask import json, jsonify
from unittest.mock import MagicMock, patch


@fixture()
def client():
    with server.app.test_client() as client:
        yield client


@patch.object(server, 'current_wall')
def test_wall(wall, client):
    wall.to_dict.return_value = {
        'name': 'some wall',
        'width': 64,
        'height': 96
    }
    resp = client.get('/wall')
    data = json.loads(resp.data)
    assert data['name'] == 'some wall'
    assert data['width'] == 64
    assert data['height'] == 96


@patch.object(server, 'current_wall')
def test_get_light(wall, client):
    resp = client.get('/light/2/3')
    wall.pixel.assert_called_once_with(2, 3)


@patch.object(server, 'current_wall')
def test_set_light(wall, client):
    resp = client.put('/light/2/3', data={
        'color': '#ff0000'
    })
    wall.set_pixel.assert_called_once_with(2, 3, '#ff0000')


@patch.object(server, 'current_wall')
def test_clear_light(wall, client):
    resp = client.delete('/light/2/3')
    wall.clear_pixel.assert_called_once_with(2, 3)


@patch.object(server, 'current_wall')
def test_get_lights(wall, client):
    wall.pixels.return_value = [['#aaaaaa'] * 3] * 2
    resp = client.get('/lights')
    data = json.loads(resp.data)
    assert len(data) == 2
    assert len(data[0]) == 3


@patch.object(server, 'current_wall')
def test_set_lights(wall, client):
    resp = client.put('/lights', json=[['#aaaaaa'] * 3] * 2)
    wall.set_pixels.assert_called_once()
    

@patch.object(server, 'current_wall')
def test_set_lights(wall, client):
    resp = client.delete('/lights')
    wall.clear_pixels.assert_called_once()