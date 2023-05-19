import secrets
import string
from datetime import datetime
from typing import Union

from django.conf import settings

from .base import RedisHelper


class CodeConfirmation(RedisHelper):
    PREFIX = 'code_confirmation'

    @staticmethod
    def generate_secret_token(length: int = 30):
        token = secrets.token_hex(length)
        t = str(int(datetime.utcnow().timestamp()))
        return token + t

    @staticmethod
    def generate_code(card_number: str = None, length: int = 6):
        if settings.DEBUG or card_number == settings.DEBUG_CARD_NUMBER:
            return settings.DEBUG_CODE
        return ''.join([secrets.choice(string.digits) for _ in range(length)])

    @classmethod
    def get_code(cls, card_number: str) -> tuple[str, str]:
        token, code = cls.generate_secret_token(), cls.generate_code(card_number)
        cls.set_data(token, dict(card_number=card_number, code=code), settings.CODE_LIFETIME)
        return token, code

    @classmethod
    def check_code(cls, token: str, code: str) -> Union[str, bool, None]:
        data = cls.get_data(token)
        if code_ := data.get('code'):
            return data.get('card_number') if str(code_) == code else False
        return
