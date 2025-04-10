import pathlib
from functools import lru_cache
from decouple import Config, RepositoryEnv, config as config_default
from django.conf import settings

BASE_DIR = pathlib.Path(__file__).parent.parent

ENV_PATH = BASE_DIR / ".env"

@lru_cache()
def get_config():
    if ENV_PATH.exists():
        print("Loading configuration from .env file.")
        return Config(RepositoryEnv(ENV_PATH))
    print("Loading default configuration.")
    return config_default

config = get_config()