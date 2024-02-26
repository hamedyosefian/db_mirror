from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # SQLALCHEMY_DATABASE_URL: str = 'sqlite:///./test.db'
    # SQLALCHEMY_DATABASE_URL: str = 'postgresql://hamedyousefian:12345678@127.0.0.1:5432/dbmirror'
    SQLALCHEMY_DATABASE_URL: str = 'postgresql://postgres:j5vDMvtbKcJGDPyoZsVhdOXFHVm7D8q37FKwP3LW1FmA8mU3IplkAK3OcfVx9CX2@192.168.0.20:9005/dbmirror'

    S3_ACCESS_KEY: str = "pAu8fSv3SkGSPk0NSbnR"
    S3_SECRET_key: str = "ENYWgxaLQ5EzMFuz0iir2dw1cGa7iI4u4k5YOfWA"
    S3_URL: str = "https://storage.mobedu.ir"

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
