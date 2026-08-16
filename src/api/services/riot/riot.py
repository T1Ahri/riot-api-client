from src.api.client import RiotAPIClient

from .endpoints import (
    AccountV1
)

class riot:
    def __init__(self, client: RiotAPIClient):
        self.client = client

        self.account = AccountV1(self.client)