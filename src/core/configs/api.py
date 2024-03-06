from pydantic.fields import Field
from pydantic_settings import BaseSettings
from pydantic_settings.main import SettingsConfigDict


class ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    title: str = Field(default=..., alias="API_TITLE")
    description: str = Field(default=..., alias="API_DESCRIPTION")


settings = ApiSettings()
