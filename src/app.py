# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from .api.client import RiotAPIClient

from .api.services import (
    AccountV1,
    ChampionMasteryV4,
    MatchV5,
    SummonerV4
)

class app:
    def __init__(self, api_key: str):
        self.client = RiotAPIClient(api_key)

        self._account = AccountV1(self.client)
        self. champion_mastery = ChampionMasteryV4(self.client)
        self.match = MatchV5(self.client)
        self.summoner = SummonerV4(self.client)