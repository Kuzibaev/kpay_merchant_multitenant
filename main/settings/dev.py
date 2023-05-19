from .base import *

SITE_URL = "http://localhost:8001"

ALLOWED_HOSTS = ['*']

MIDDLEWARE += []

INSTALLED_APPS += [
    'auto_populate'
]

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'login': '100/day'
}

SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = timedelta(days=15)
SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'] = timedelta(days=30)

STATIC_ROOT = BASE_DIR / 'cdn_local' / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'cdn_local' / 'media'

INTERNAL_IPS = [
    "127.0.0.1",
]
