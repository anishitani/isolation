import uuid

from entities import GameEntity


class GameRepository():
    def __init__(self):
        self._games = {}

    def createGame(self):
        game = GameEntity.GameEntity(id=str(uuid.uuid4()))
        self._games[game.id] = game
        return game.id

    def getGames(self):
        keys = self._games.keys()
        if len(list(keys)) > 0:
            return list(keys)
        else:
            return ""

    def getGame(self, id):
        return self._games[id].serialize()
