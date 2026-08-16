# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from src.api.client import RiotAPIClient
from ...urls.endpoints import Region
from ...urls.endpoints import (
    match_ids_by_puuid_url,
    match_ids_params,
    match_detail_by_matchId_url,
    match_timeline_by_matchId_url
)

class MatchV5:
    def __init__(self, client: RiotAPIClient):
        self.client = client

    def get_match_ids_by_puuid(
            self,
            region: Region,
            puuid: str,
            start_time: int = None,
            end_time: int = None,
            queue: int = None,
            type: str = None,
            start: int = None,
            count: int = None
    ) -> list:
        url = match_ids_by_puuid_url(region, puuid)
        params = match_ids_params(
            start_time,
            end_time,
            queue,
            type,
            start,
            count
        )
        return self.client.get(url, params)

    def get_detail_by_matchId(
            self,
            region: Region,
            match_id: str
    ) -> dict:
        url = match_detail_by_matchId_url(region, match_id)
        return self.client.get(url)

    def get_timeline_by_matchId(
            self,
            region: Region,
            match_id: str
    ) -> dict:
        url = match_timeline_by_matchId_url(region, match_id)
        return self.client.get(url)