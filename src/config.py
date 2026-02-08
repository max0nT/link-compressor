import pydantic_settings

class Config(pydantic_settings.BaseSettings):
    """Config for backend app."""

    model_config = pydantic_settings.SettingsConfigDict(
        env_file="src/.env",
        extra="ignore",
    )

    token_url_length: int
    sqlite3_db : str = "database.db"

settings = Config()
