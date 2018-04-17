#!/usr/bin/env python3
"""
Author: André Nishitani <atoshio25@gmail.com>

This is a Isolation Game Server intended to provide a platform for intelligent
game playing algorithms.
"""
import os

from flask import Flask, Blueprint

import Settings

from controllers.GameController import blueprint_game

app = Flask(__name__)


def initialize_app(flask_app):
    prefix = '/isolation/api/v{}'.format(Settings.ISOLATION_VERSION[:1])
    blueprint = Blueprint('api', __name__, url_prefix=prefix)
    flask_app.register_blueprint(blueprint)
    flask_app.register_blueprint(blueprint_game)


def main(flask_app):
    port = int(os.environ.get("PORT", 8000))
    initialize_app(flask_app)
    app.run(host="0.0.0.0", port=port, debug=True)


if __name__ == "__main__":
    main(app)
