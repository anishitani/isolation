from flask import Blueprint, request, jsonify

from services import GameService
from utils.json.DefaultResponse import DefaultResponse

blueprint_game = Blueprint('games', __name__, url_prefix="/games")
gameService = GameService.GameService()


@blueprint_game.route("", methods=["GET", "POST"])
def games():
    if request.method == "POST":
        response = DefaultResponse(status=True, message="Game created successfully", result=gameService.createGame())
        return jsonify(response.serialize())
    elif request.method == "GET":
        response = DefaultResponse(status=True, message="Games retrieved successfully", result=gameService.getGames())
        return jsonify(response.serialize())


@blueprint_game.route("/<id>", methods=["GET"])
def game(id):
    response = DefaultResponse(status=True, message="Game retrieved successfully", result=gameService.getGame(id))
    return jsonify(response.serialize())
