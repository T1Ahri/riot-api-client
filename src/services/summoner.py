# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from src.api.client import RiotAPIClient
from src.api.endpoints import Platform, summoner_by_puuid_url

class SummonerService:
    def __init__(self, client: RiotAPIClient):
        self.client = client

    def get_summoner_by_puuid(self, region: Platform, puuid: str) -> dict:
        url = summoner_by_puuid_url(region, puuid)
        response = self.client.get(url)
        return response