# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

from ...endpoint import Endpoint

class RiotEndpoint(Endpoint):
    def __init__(self, url: str):
        full_url = f"/riot{url}"
        super().__init__(full_url)

class AccountV1Endpoint(RiotEndpoint):
    def __init__(self, url: str):
        full_url = f"/account/v1{url}"
        super().__init__(full_url)