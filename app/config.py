from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = 'sqlite:///./test.db'

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
