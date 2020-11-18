from django.apps import apps
from django.conf import settings

__version__ = '0.1.0.dev'


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


def get_model(model, app_label=None):
    model = model.lower()
    if app_label:
        if app_label not in apps.all_models:
            raise ValueError(f'App not found ({app_label})')
        if model in apps.all_models[app_label]:
            return apps.all_models[app_label][model]

        raise KeyError(f'Model not found ({model} in {app_label})')

    for app in apps.all_models:
        if model in apps.all_models[app]:
            return apps.all_models[app][model]

    raise KeyError(f'Model not found ({model})')
