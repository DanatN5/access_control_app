from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AmqpDsn, PostgresDsn

class BrokerConfig(BaseSettings):
    url: AmqpDsn = "amqp://guest:guest@localhost:5672/"
    queue: str = "validated_requests"

class DatabaseConfig(BaseSettings):
    url: PostgresDsn


class Settings(BaseSettings):

    db: DatabaseConfig
    broker: BrokerConfig = BrokerConfig()

    DEBUG: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
        case_sensitive=False
        )


settings = Settings()
