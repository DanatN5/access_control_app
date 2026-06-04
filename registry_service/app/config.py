from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    POSTGRES_DB: str = "access_control_service_db"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str
    DATABASE_URL: str


    DEBUG: bool = True

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
