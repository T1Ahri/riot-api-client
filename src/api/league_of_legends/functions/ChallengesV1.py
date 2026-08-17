# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from src.api.client import RiotAPIClient

class ChallengesV1:
    def __init__(self, client: RiotAPIClient):
            self.client = client