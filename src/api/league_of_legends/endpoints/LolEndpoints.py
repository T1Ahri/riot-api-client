from ...endpoint import Endpoint

class LolEndpoint(Endpoint):
    def __init__(self, url: str):
        full_url = f"/lol{url}"
        super().__init__(full_url)

class ChampionMasteryV4Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/champion-mastery/v4{url}"
        super().__init__(url)

class MatchV5Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/match/v5{url}"
        super().__init__(url)

class SummonerV4Endpoint(LolEndpoint):
    def __init__(self, url: str):
        full_url = f"/summoner/v4{url}"
        super().__init__(url)