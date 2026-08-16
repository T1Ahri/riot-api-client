# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from src.api.client import RiotAPIClient
from ...urls.endpoints import Platform
from ..endpoints.LolUrls import ChampionMasteryV4Urls

class ChampionMasteryV4:
    def __init__(self, client: RiotAPIClient):
        self.client = client

    def get_all_champ_mastery_entries_by_puuid(
            self,
            region: Platform,
            puuid: str
    ) -> list:
        url = ChampionMasteryV4Urls.all_champ_mastery_entries_by_puuid()
        response = self.client.get(url)
        return response

    def get_champ_mastery_entrie_by_puuid_champId(
            self,
            region: Platform,
            puuid: str,
            champ_id: int
    ) -> dict:
        url = ChampionMasteryV4Urls.champ_mastery_entrie_by_puuid_champ_id()
        response = self.client.get(url)
        return response

    def get_top_champ_mastery_entries_by_puuid(
            self,
            region: Platform,
            puuid: str,
            **kwargs
    ) -> list:
        url = ChampionMasteryV4Urls.top_champ_mastery_entries_by_puuid()
        params = top_champ_mastery_entries_params(**kwargs)
        response = self.client.get(url, params)
        return response

    def get_total_champ_mastery_score_by_puuid(
            self,
            region: Platform,
            puuid: str
    ) -> int:
        url = ChampionMasteryV4Urls.total_champ_mastery_score_by_puuid()
        response = self.client.get(url)
        return response