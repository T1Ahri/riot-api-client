# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from src.api.client import RiotAPIClient
from src.api.services.urls.endpoints import Platform
from src.api.services.urls.endpoints import (
    all_champ_mastery_entries_by_puuid_url,
    champ_mastery_entrie_by_puuid_champId_url,
    top_champ_mastery_entries_by_puuid_url,
    top_champ_mastery_entries_params,
    total_champ_mastery_score_by_puuid
)

class ChampionMasteryV4:
    def __init__(self, client: RiotAPIClient):
        self.client = client

    def get_all_champ_mastery_entries_by_puuid(self, region: Platform, puuid: str) -> list:
        url = all_champ_mastery_entries_by_puuid_url(region, puuid)
        response = self.client.get(url)
        return response

    def get_champ_mastery_entrie_by_puuid_champId(self, region: Platform, puuid: str, champ_id: int) -> dict:
        url = champ_mastery_entrie_by_puuid_champId_url(region, puuid, champ_id)
        response = self.client.get(url)
        return response

    def get_top_champ_mastery_entries_by_puuid(self, region: Platform, puuid: str, **kwargs) -> list:
        url = top_champ_mastery_entries_by_puuid_url(region, puuid)
        params = top_champ_mastery_entries_params(**kwargs)
        response = self.client.get(url, params)
        return response

    def get_total_champ_mastery_score_by_puuid(self, region: Platform, puuid: str) -> int:
        url = total_champ_mastery_score_by_puuid(region, puuid)
        response = self.client.get(url)
        return response