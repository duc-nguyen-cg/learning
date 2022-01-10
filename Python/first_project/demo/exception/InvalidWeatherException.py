class InvalidWeatherException(Exception):
    def __init__(self, payload = None):
        self.payload = payload
        self.message = "{} is an invalid Weather"

    def __str__(self) -> str:
        return str(self.message.format(self.payload))