# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from src.api.client import RiotAPIClient

from src.api.services import (
    lol,
    lor,
    riftbound,
    riot,
    tft,
    val
)

class app:
    def __init__(self, api_key: str):
        self.client = RiotAPIClient(api_key)

        self.lol = lol(self.client)
        self.riot = riot(self.client)