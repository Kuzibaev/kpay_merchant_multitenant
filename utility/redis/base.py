import json

from django.core.cache import cache


class RedisHelper:
    PREFIX: str
    DELIMITER: str = ':'

    @classmethod
    def _make_cache_key(cls, unique_str: str, get_prefix_only: bool = False):
        parts = [
            cls.PREFIX,
        ]
        if get_prefix_only:
            return cls.DELIMITER.join(parts)
        return cls.DELIMITER.join([*parts, unique_str])

    @classmethod
    def set_data(cls, key: str, data: dict, ex: int):
        cache.set(cls._make_cache_key(key), json.dumps(data), ex)

    @classmethod
    def get_data(cls, key: str):
        data = cache.get(cls._make_cache_key(key), default="{}")
        try:
            data = json.loads(data)
            return data
        except json.JSONDecodeError:
            return {}
