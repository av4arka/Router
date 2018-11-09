class InvalidIPv4Address(Exception):


    def __init__(self, text):
        InvalidIPv4Address.text = text


class InvalidNetwork(Exception):


    def __init__(self, text):
        InvalidNetwork.text = text