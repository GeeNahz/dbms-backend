from .config import *
from utils.get_env_wrapper import get_env_value

DEBUG = False
SECRET_KEY = get_env_value('SECRET_KEY')
# TODO: SECURITY WARNING: update this when there is a production host
ALLOWED_HOSTS = ["0.0.0.0", "localhost", "example.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_env_value("DATABASE_NAME"),
        "USER": get_env_value("DATABASE_USER"),
        "PASSWORD": get_env_value("DATABASE_PASSWORD"),
        "HOST": get_env_value("DATABASE_HOST"),
        "PORT": get_env_value("DATABASE_PORT"),
        "OPTIONS": {
            "sslmode": "require",
        }
    }
}
