# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from .LolEndpoints import (
    ChampionMasteryV4Endpoint,
    MatchV5Endpoint,
    SummonerV4Endpoint
)

class ChampionMasteryV4Urls:
    all_champ_mastery_entries_by_puuid = ChampionMasteryV4Endpoint("/champion-masteries/by-puuid/{puuid}")
    champ_mastery_entrie_by_puuid_champ_id = ChampionMasteryV4Endpoint("/champion-masteries/by-puuid/{puuid}/by-champion/{champ_id}")
    top_champ_mastery_entries_by_puuid = ChampionMasteryV4Endpoint("/champion-masteries/by-puuid/{puuid}/top")
    total_champ_mastery_score_by_puuid = ChampionMasteryV4Endpoint("/scores/by-puuid/{puuid}")

class MatchV5Urls:
    match_ids_by_puuid = MatchV5Endpoint("/matches/by-puuid/{puuid}/ids")
    match_detail_by_match_id = MatchV5Endpoint("/matches/{match_id}")
    match_timeline_by_match_id = MatchV5Endpoint("/matches/{match_id}/timeline")

class SummonerV4Urls:
    summoner_by_puuid = SummonerV4Endpoint("/summoners/by-puuid/{puuid}")