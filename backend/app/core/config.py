from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "NBA Legacy Universe Tracker API"
    debug: bool = True
    database_url: str = "postgresql+psycopg2://legacy:legacy@db:5432/legacy_universe"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="API_")


settings = Settings()
