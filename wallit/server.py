"""REST Server API for controlling wall."""
from flask import Flask, request

app = Flask(__name__)
current_wall = None


@app.route('/wall')
def wall():
    return current_wall.to_dict()