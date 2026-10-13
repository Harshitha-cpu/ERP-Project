from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# planforge/.env  (this file lives at planforge/backend/app/core/config.py)
ROOT_ENV = Path(__file__).resolve().parents[3] / ".env"


class Settings(BaseSettings):
    app_name: str = "PlanForge"
    environment: str = "development"
    database_url: str

    # extra="ignore" lets .env contain POSTGRES_* values used only by Docker
    model_config = SettingsConfigDict(env_file=ROOT_ENV, extra="ignore")


settings = Settings()