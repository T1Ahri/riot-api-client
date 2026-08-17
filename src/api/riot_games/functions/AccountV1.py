# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from src.api.client import RiotAPIClient
from ...urls.endpoints import Region
from ..tools.RiotUrls import (
    AccountV1Urls
)

class AccountV1:
    def __init__(self, client: RiotAPIClient):
        self.client = client

    def get_puuid_by_riot_id(
            self,
            region: Region,
            game_name: str,
            tag_line: str
    ) -> str:
        url = AccountV1Urls.account_by_riot_id(region, game_name=game_name, tag_line=tag_line)
        response = self.client.get(url)
        return response