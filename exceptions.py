class MainException(Exception):

    def __init__(self, text):
        MainException.text = text

class InvalidIPv4Address(MainException):
    pass

class InvalidNetwork(MainException):
    pass

class InvalidRoute(MainException):
    pass

class InvalidRouter(MainException):
    pass
