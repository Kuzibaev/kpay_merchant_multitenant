from django.conf import settings


def get_media_url(path: str):
    return settings.SITE_URL + path
