# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from ...endpoint import Endpoint

class LolEndpoint(Endpoint):
    def __init__(self, url: str):
        full_url = f"/lol{url}"
        super().__init__(full_url)

class ChallengesV1Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/challenges/v1{url}"
        super().__init__(full_url)

class ChampionMasteryV4Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/champion-mastery/v4{url}"
        super().__init__(full_url)

class ChampionV3Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/platform/v3{url}"
        super().__init__(full_url)

class ClashV1Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/clash/v1{url}"
        super().__init__(full_url)

class LeagueExpV4Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/league-exp/v4{url}"
        super().__init__(full_url)

class LeagueV4Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/league/v4{url}"
        super().__init__(full_url)

class MatchV5Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/match/v5{url}"
        super().__init__(full_url)

class SpectatorV5Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/spectator/v5{url}"
        super().__init__(full_url)

class StatusV4Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/status/v4{url}"
        super().__init__(full_url)

class SummonerV4Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/summoner/v4{url}"
        super().__init__(full_url)