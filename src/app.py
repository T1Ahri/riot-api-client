# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from .api import RiotAPIClient

from .api import (
    Lol,
    Lor,
    Riot,
    Tft,
    Val
)

class app:
    def __init__(self, api_key: str):
        self.client = RiotAPIClient(api_key)

        self.lol = Lol(self.client)
        self.riot = Riot(self.client)