#!/usr/bin/env python3
"""
Documentation

See also https://www.python-boilerplate.com/flask
"""
import os

from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route("/games")
class Games(Resource):
    def post(self):
        return {"gameid": "hash"}
    def put(self):
        return {"action": "update game"}

@api.route('/games/<id>')
class Game(Resource):
    def get(self, id):
        return {"action": "current state"}
    def delete(self, id):
        return {"action": "abort game"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
