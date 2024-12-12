import random

RESPONSE_ROWS_PER_SERVER_MAX = 2000
RESPONSE_ROWS_PER_SERVER_MIN = 200
PRICE_DIFFERENCE_PCT = 5
REQUEST_TIMEOUT = 5  # in seconds
RESPONSE_DELAY_MAX = 10  # in seconds
MIN_PORT = 10001
MAX_PORT = 10055
FAILED_PORTS = [10002, 10003, 10006]

class Ports:
    def __init__(self, min_port, max_port, failed_ports):
        self.min = min_port
        self.max = max_port
        self.failed = failed_ports

    @staticmethod
    def get_ports():
        return Ports(MIN_PORT, MAX_PORT, FAILED_PORTS)


class Response:
    def __init__(self, dex, responses):
        self.dex = dex
        self.responses = responses


class ResponseRow:
    def __init__(self, timestamp, price, supply, address):
        self.timestamp = timestamp
        self.price = price
        self.supply = supply
        self.address = address


def random_int(min_value, max_value):
    return random.randint(min_value, max_value)
