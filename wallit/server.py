"""REST Server API for controlling wall."""
from flask import Flask, request, jsonify
from .lighting.abstract import Color
import numpy as np

app = Flask(__name__)
current_wall = None


def as_color_matrix(data):
    matrix = np.ndarray((len(data), len(data[0])), dtype='object')
    for y, row in enumerate(data):
        for x, data in enumerate(row):
            matrix[y][x] = Color.from_string(data)

    return matrix


@app.route('/wall')
def wall():
    return current_wall.to_dict()


@app.route('/light/<int:x>/<int:y>', methods=['GET', 'PUT', 'DELETE'])
def light(x, y):
    if request.method == 'PUT':
        current_wall.set_pixel(x, y, Color.from_hex(request.form['color']))
    elif request.method == 'DELETE':
        current_wall.clear_pixel(x, y)
    else:
        return current_wall.pixel(x, y)


@app.route('/lights', methods=['GET', 'PUT', 'DELETE'])
def lights():
    if request.method == 'PUT':
        matrix = as_color_matrix(request.get_json())
        current_wall.set_pixels(matrix)
    elif request.method == 'DELETE':
        current_wall.clear_pixels()
    else:
        return jsonify(current_wall.pixels())