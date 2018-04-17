from entities import GameEntity


class GameRepository():
    def __init__(self):
        self._games = {}

    def getGames(self):
        keys = self._games.keys()
        if len(list(keys)) > 0:
            return list(keys)
        else:
            return ""

    def createGame(self):
        game = GameEntity.GameEntity()
        self._games[game.id] = game
        return game.id

    def getGame(self, id):
        return self._games[id]
