class GameEntity():
    _id = None

    def __init__(self, id=None):
        self._id = id

    def serialize(self):
        return {
            "id": self._id
        }

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id
