class DefaultResponse():
    def __init__(self, status=False, message=None, result=None):
        self._status = status
        self._message = message
        self._result = result

    def serialize(self):
        return {
            "status": self._status,
            "message": self._message,
            "result": self._result
        }

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def result(self):
        return self._result

    @message.setter
    def message(self, result):
        self._result = result
