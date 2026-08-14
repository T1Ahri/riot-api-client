from src.config import RIOT_API_KEY

from src.api.rate_limiter import RateLimiter
from src.api.exceptions import *

import requests
import time

ERROR_MAP = {
    400: BadRequestError,
    401: UnauthorizedError,
    403: InvalidAPIKeyError,
    404: ResourceNotFoundError,
    405: MethodNotAllowedError,
    415: UnsupportedMediaTypeError,
    500: InternalServerError,
    502: BadGatewayError,
    503: ServiceUnavailableError,
    504: GatewayTimeoutError
}

class RiotAPIClient:
    def __init__(self):
        self.headers = {'X-Riot-Token': RIOT_API_KEY}

    def get(self, url: str, params: dict | None = None) -> dict:
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 1))
            print(f"Erreur 429 (Rate limit exceeded): Veuillez attendre {retry_after} secondes...")
            time.sleep(retry_after)
            return self.get(url, params)

        if response.status_code in ERROR_MAP:
            except_class = ERROR_MAP[response.status_code]
            raise except_class(f"Erreur {response.status_code} sur {url}", status_code=response.status_code)
        
        return response.json()