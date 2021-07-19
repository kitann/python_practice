class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened():
            raise InvalidOperationError("Stream already OPENED")
        self.opened = True

    def close(self):
        if not self.opened():
            raise InvalidOperationError("Stream already CLOSED")
        self.opened = False
