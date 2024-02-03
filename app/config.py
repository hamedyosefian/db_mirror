from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # SQLALCHEMY_DATABASE_URL: str = 'sqlite:///./test.db'
    SQLALCHEMY_DATABASE_URL: str = 'postgresql://cls5xr4af0020a5ow3jn0aoh9:c3TOywSIpWzA2UpeOdquc8Ay@192.168.0.20:9003/dbmirror'

    S3_ACCESS_KEY: str = "pAu8fSv3SkGSPk0NSbnR"
    S3_SECRET_key: str = "ENYWgxaLQ5EzMFuz0iir2dw1cGa7iI4u4k5YOfWA"
    S3_URL: str = "https://storage.mobedu.ir"

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
