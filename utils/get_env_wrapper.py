import os

from django.core.exceptions import ImproperlyConfigured

def get_env_value(env_variable: str) -> str:
    try:
        return os.environ[env_variable]
    except KeyError:
        error_msg = "Set the environment variable."
        raise ImproperlyConfigured(error_msg)