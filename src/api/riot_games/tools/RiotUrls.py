# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from .RiotEndpoints import (
    AccountV1Endpoint
)

class AccountV1Urls:
    account_by_puuid = AccountV1Endpoint("/accounts/by-puuid/{puuid}")
    account_by_riot_id = AccountV1Endpoint("/accounts/by-riot-id/{game_name}/{tag_line}")
    active_region_by_game_puuid = AccountV1Endpoint("/region/by-game/{game}/by-puuid/{puuid}")