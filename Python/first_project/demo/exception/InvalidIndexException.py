class InvalidIndexException(Exception):
    def __init__(self, payload = None):
        self.payload = payload
        self.message = "{} is invalid index"

    def __str__(self) -> str:
        return str(self.message.format(self.payload))
        
        