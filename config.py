from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8"
    )

    bot_token: str
    admin_ids: frozenset[int] = frozenset({42, 3595399})


settings = Settings()