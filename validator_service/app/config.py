from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AmqpDsn

class BrokerConfig(BaseSettings):
    url: AmqpDsn = "amqp://guest:guest@localhost:5672/"
    queue: str = "requests"


class Settings(BaseSettings):

    broker: BrokerConfig = BrokerConfig()
    request_url: str

    DEBUG: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
        case_sensitive=False
        )


settings = Settings()