from django.conf import settings


def get_setting(attr: str, *fields):
    if not hasattr(settings, attr):
        return None

    value = getattr(settings, attr)
    for field in fields:
        try:
            value = value[field]
        except KeyError:
            return None

    return value
