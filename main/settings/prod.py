from .base import *

REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
    'login': '100/day'
}
ALLOWED_HOSTS = ['*']
SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'] = timedelta(days=15)
SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'] = timedelta(days=30)
STATIC_ROOT = BASE_DIR / 'cdn' / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'cdn' / 'media'
