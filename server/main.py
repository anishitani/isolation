#!/usr/bin/env python3
"""
Documentation

See also https://www.python-boilerplate.com/flask
"""
import os

from flask import Flask, Blueprint

import Settings
from handlers.ApiHandler import api
from controllers.GameController import resource as GameResource

app = Flask(__name__)


def initialize_app(flask_app):
    prefix = '/isolation/api/v{}'.format(Settings.ISOLATION_VERSION[:1])
    blueprint = Blueprint('api', __name__, url_prefix=prefix)
    api.init_app(blueprint)
    api.add_namespace(GameResource)
    flask_app.register_blueprint(blueprint)


def main(flask_app):
    port = int(os.environ.get("PORT", 8000))
    initialize_app(flask_app)
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main(app)
