# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

class Region:
    AMERICAS = "americas"
    ASIAS = "asia"
    EUROPE = "europe"
    SEAS = "sea"

class Platform:
    EUW1 = "euw1"
    


# --- ACCOUNT-V1 ---

def account_by_puuid_url(region: Region, puuid: str) -> dict:
    return f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"

def account_by_riotId_url(region: Region, game_name: str, tag_line: str) -> str:
    return f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"


# --- CHAMPION-MASTERY-V4 ---

def all_champ_mastery_entries_by_puuid_url(region: Platform, puuid: str) -> list:
    return f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}"

def champ_mastery_entrie_by_puuid_champId_url(region: Platform, puuid: str, champ_id: int) -> dict:
    return f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champ_id}"

def top_champ_mastery_entries_by_puuid_url(region: Platform, puuid: str) -> list:
    return f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top"

def top_champ_mastery_entries_params(count: int | None = None) -> dict:
    params = {
        'count': count
    }
    return {key: value for key, value in params.items() if value is not None}

def total_champ_mastery_score_by_puuid(region: Platform, puuid: str) -> int:
    return f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/scores/by-puuid/{puuid}"


# --- MATCH-V5 ---

def match_ids_by_puuid_url(region: str, puuid: str) -> str:
    return f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"

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

def match_detail_by_matchId_url(region: str, match_id: int) -> str:
    return f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

def match_timeline_by_matchId_url(region: str, match_id: int) -> str:
    return f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline"


# --- SUMMONER-V4 ---

def summoner_by_puuid_url(region: Platform, puuid: str) -> dict:
    return f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"