# Copyright (C) 2026 T1Ahri
# Licensed under the GNU Affero General Public License v3.0
# See LICENSE file for details

class RiotAPIError(Exception):
    def __init__(self, message: str, status_code: int | None = None):
        self.status_code = status_code
        super().__init__(message)


# --- 4xx : erreurs côté client

class BadRequestError(RiotAPIError):                    # 400
    pass

class UnauthorizedError(RiotAPIError):                  # 401
    pass

class InvalidAPIKeyError(RiotAPIError):                 # 403
    pass

class ResourceNotFoundError(RiotAPIError):              # 404
    pass

class MethodNotAllowedError(RiotAPIError):              # 405
    pass

class UnsupportedMediaTypeError(RiotAPIError):          # 415
    pass

class RateLimitExceededError(RiotAPIError):             # 429
    pass


# --- 5xx : erreur côté API

class InternalServerError(RiotAPIError):                # 500
    pass

class BadGatewayError(RiotAPIError):                    # 502
    pass

class ServiceUnavailableError(RiotAPIError):            # 503
    pass

class GatewayTimeoutError(RiotAPIError):                # 504
    pass