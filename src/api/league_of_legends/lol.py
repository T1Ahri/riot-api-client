# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from src.api.client import RiotAPIClient

from .functions import (
    ChampionMasteryV4,
    MatchV5,
    SummonerV4
)

class Lol:
    def __init__(self, client: RiotAPIClient):
        self.client = client

        self.champion_mastery = ChampionMasteryV4(self.client)
        self.match = MatchV5(self.client)
        self.summoner = SummonerV4(self.client)