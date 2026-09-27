"""Configuration loaded from environment variables (see .env)."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App settings. Every UPPERCASE field maps to a key in .env."""

    APP_NAME: str = "Byte2Bite"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Comma-separated list of allowed frontend origins
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    """Cached so .env is read once, not on every request."""
    return Settings()
