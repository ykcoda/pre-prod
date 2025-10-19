from pydantic_settings import BaseSettings, SettingsConfigDict
import os

# Base config ref for  env varibles
_base_config = SettingsConfigDict(
    env_file="./app/.env", env_ignore_empty=True, extra="ignore"
)


# Database settings class
class DatabaseSettings(BaseSettings):
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST") or ""
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT") or 0)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB") or ""
    POSTGRES_USER: str = os.getenv("POSTGRES_USER") or ""
    POSTGRES_PASS: str = os.getenv("POSTGRES_PASS") or ""

    
    model_config = _base_config

    # Database Url
    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


# Instatiating Database Settings
db_settings = DatabaseSettings()

