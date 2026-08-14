# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from src.api.client import RiotAPIClient
from src.api.endpoints import Region, account_by_riotId_url

class AccountService:
    def __init__(self, client: RiotAPIClient):
        self.client = client

    def get_puuid_by_riotId(self, region: Region, game_name: str, tag_line: str) -> str:
        url = account_by_riotId_url(region, game_name, tag_line)
        response = self.client.get(url)
        return response['puuid']