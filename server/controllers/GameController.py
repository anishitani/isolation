from flask_restplus import Resource

from handlers.ApiHandler import api

resource \
    = api.namespace('games', description='Operations related to game actions')


@resource.route("/")
class Games(Resource):
    def post(self):
        return {"gameid": "hash"}

    def put(self):
        return {"action": "update game"}


@resource.route('/<id>')
class Game(Resource):
    def get(self, id):
        return {"action": "current state"}

    def delete(self, id):
        return {"action": "abort game"}
