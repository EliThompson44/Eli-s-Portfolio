import os


class Settings:
    app_name: str = "NBA Legacy Universe Tracker API"
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://nba_user:nba_pass@localhost:5432/nba_legacy",
    )


settings = Settings()
