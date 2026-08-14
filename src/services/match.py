from src.api.client import RiotAPIClient
from src.api.endpoints import Region, match_ids_by_puuid_url, matchs_ids_params, match_detail_by_matchId_url, match_timeline_by_matchId_url

class MatchService:
    def __init__(self, client: RiotAPIClient):
        self.client = client

    def get_match_ids_by_puuid(self, region: Region, puuid: str, **kwargs) -> list:
        url = match_ids_by_puuid_url(region, puuid)
        params = matchs_ids_params(**kwargs)
        return self.client.get(url, params=params)

    def get_detail_by_matchId(self, region: Region, match_id: str) -> dict:
        url = match_detail_by_matchId_url(region, match_id)
        return self.client.get(url)

    def get_timeline_by_matchId(self, region: Region, match_id: str) -> dict:
        url = match_timeline_by_matchId_url(region, match_id)
        return self.client.get(url)