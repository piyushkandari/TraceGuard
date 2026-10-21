"""Application configuration."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Global settings loaded from environment variables."""
    app_name: str = "Aegis Scan API"
    environment: str = "local"
    database_url: str = "postgresql://scanner:scannerpass@localhost:5432/scanner_db"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()