from .base import RedisHelper


class JWTToken(RedisHelper):
    PREFIX = 'jwt-token'

    @classmethod
    def is_blacklisted(cls, token: str):
        if cls.get_data(token):
            return True
        return False

    @classmethod
    def blacklist_token(cls, token: str, ex: int):
        cls.set_data(token, dict(blacklisted=True), ex=ex)
