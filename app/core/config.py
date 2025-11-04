"""Application configuration using Pydantic settings."""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator


class Settings(BaseSettings):
    """Centralised application settings loaded from environment variables."""

    # Application
    app_name: str = "Reserva Labs API"
    environment: str = "development"
    debug: bool = True
    
    # Database
    database_url: str
    sqlalchemy_echo: bool = False
    
    # Security
    # jwt_secret_key: str
    # jwt_algorithm: str = "HS256"
    # access_token_expire_minutes: int = 30
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="allow",
    )

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, value: str) -> str:
        """Validate that DATABASE_URL is properly formatted."""
        if not value:
            raise ValueError("DATABASE_URL must be set")
        if not value.startswith("postgresql"):
            raise ValueError("DATABASE_URL must be a PostgreSQL connection string")
        return value

    @property
    def sync_database_url(self) -> str:
        """Return a synchronous-compatible database URL (used by Alembic)."""
        if "+asyncpg" in self.database_url:
            return self.database_url.replace("+asyncpg", "")
        return self.database_url


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings instance."""
    return Settings()
