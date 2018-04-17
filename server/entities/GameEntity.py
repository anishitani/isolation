import uuid


class GameEntity():
    id = ''

    def __init__(self):
        self.id = str(uuid.uuid4())
