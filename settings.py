# settings.py
from pydantic_settings import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @validator("ENVIRONMENT")
    def validate_environment(cls, value):
        if value not in ["dev", "test", "prod"]:
            raise ValueError("ENVIRONMENT must be one of (dev, test, prod)")
        return value
