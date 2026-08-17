# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from .LolEndpoints import (
    ChallengesV1Endpoint,
    ChampionMasteryV4Endpoint,
    ChampionV3Endpoint,
    ClashV1Endpoint,
    LeagueExpV4Endpoint,
    LeagueV4Endpoint,
    MatchV5Endpoint,
    SpectatorV5Endpoint,
    StatusV4Endpoint,
    SummonerV4Endpoint
)

class ChallengesV1Urls:
    end = ChallengesV1Endpoint("")
    end = ChallengesV1Endpoint("")
    end = ChallengesV1Endpoint("")
    end = ChallengesV1Endpoint("")
    end = ChallengesV1Endpoint("")
    end = ChallengesV1Endpoint("")

class ChampionMasteryV4Urls:
    all_champ_mastery_entries_by_puuid = ChampionMasteryV4Endpoint("/champion-masteries/by-puuid/{puuid}")
    champ_mastery_entry_by_puuid_champ_id = ChampionMasteryV4Endpoint("/champion-masteries/by-puuid/{puuid}/by-champion/{champ_id}")
    top_champ_mastery_entries_by_puuid = ChampionMasteryV4Endpoint("/champion-masteries/by-puuid/{puuid}/top")
    total_champ_mastery_score_by_puuid = ChampionMasteryV4Endpoint("/scores/by-puuid/{puuid}")

class ChampionV3Urls:
    champion_rotations = ChampionV3Endpoint("/champion-rotations")

class ClashV1Urls:
    end = ClashV1Endpoint("")
    end = ClashV1Endpoint("")
    end = ClashV1Endpoint("")
    end = ClashV1Endpoint("")
    end = ClashV1Endpoint("")

class LeagueExpV4Urls:
    all_league_entries = LeagueExpV4Endpoint("/entries/{queue}/{tier}/{division}")

class LeagueV4Urls:
    challenger_by_queue = LeagueV4Endpoint("/challengerleagues/by-queue/{queue}")
    all_league_entries_by_puuid = LeagueV4Endpoint("/entries/by-puuid/{puuid}")
    all_league_entries = LeagueV4Endpoint("/entries/{queue}/{tier}/{division}")
    grand_master_by_queue = LeagueV4Endpoint("/grandmasterleagues/by-queue/{queue}")
    master_by_queue = LeagueV4Endpoint("/masterleagues/by-queue/{queue}")

class MatchV5Urls:
    match_ids_by_puuid = MatchV5Endpoint("/matches/by-puuid/{puuid}/ids")
    player_replays_by_puuid = MatchV5Endpoint("/matches/by-puuid/{puuid}/replays")
    match_detail_by_match_id = MatchV5Endpoint("/matches/{match_id}")
    match_timeline_by_match_id = MatchV5Endpoint("/matches/{match_id}/timeline")

class SpectatorV5Urls:
    current_game_detail_by_puuid = SpectatorV5Endpoint("/active-games/by-summoner/{puuid}")

class StatusV4Urls:
    lol_status = StatusV4Endpoint("/platform-data")

class SummonerV4Urls:
    summoner_detail_by_puuid = SummonerV4Endpoint("/summoners/by-puuid/{puuid}")