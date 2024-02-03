from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = 'sqlite:///./test.db'

    S3_ACCESS_KEY: str = "pAu8fSv3SkGSPk0NSbnR"
    S3_SECRET_key: str = "ENYWgxaLQ5EzMFuz0iir2dw1cGa7iI4u4k5YOfWA"
    S3_URL: str = "https://storage.mobedu.ir"

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
