from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    symbol: str = "-",
    min_len: int = 7,
    max_len: int = 10,
    delay: float = 2.0

model_config = SettingsConfigDict(
env_file=".env",
env_file_encoding="utf-8"
)

settings = Setting()
