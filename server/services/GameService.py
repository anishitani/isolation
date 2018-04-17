from repositories import GameRepository


class GameService():
    def __init__(self):
        self._repo = GameRepository.GameRepository()

    def createGame(self):
        return self._repo.createGame()

    def getGames(self):
        return self._repo.getGames()
