# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

class Region:
    AMERICAS = "americas"
    ASIAS = "asia"
    EUROPE = "europe"
    SEAS = "sea"

#class Platform:
    


# --- ACCOUNT-V1 ---

def account_by_riotId_url(region: Region, game_name: str, tag_line: str) -> str:
    return f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"


# --- SUMMONER-V4 ---

#def summoner_by_puuid_url(region)


# --- MATCH-V5 ---

def matchs_ids_params(start_time: int | None = None, end_time: int | None = None, queue: int | None = None, type: str | None = None, start: int | None = None, count: int | None = None) -> dict:
    params = {
        'startTime': start_time,
        'endTime': end_time,
        'queue': queue,
        'type': type,
        'start': start,
        'count': count
    }
    return {key: value for key, value in params.items() if value is not None}

def match_ids_by_puuid_url(region: str, puuid: str, ) -> str:
    return f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"

def match_detail_by_matchId_url(region: str, match_id: int) -> str:
    return f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

def match_timeline_by_matchId_url(region: str, match_id: int) -> str:
    return f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline"