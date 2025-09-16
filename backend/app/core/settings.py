from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
api_v1_prefix: str = "/api/v1"
postgres_dsn: str
redis_url: str = "redis://redis:6379/0"
deepseek_token: str
allowed_origins: list[str] = ["*"]


class Config:
env_file = "../../.env"


@lru_cache
def get_settings():
return Settings()