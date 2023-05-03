import os

from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings, SecretStr, StrictStr

load_dotenv(find_dotenv())


class TGSettings(BaseSettings):
    tg_api_key: SecretStr = os.getenv('TOKEN', None)


class SiteSettings(BaseSettings):
    api_key: SecretStr = os.getenv('SITE_API', None)
    host_api: StrictStr = os.getenv('HOST_API', None)