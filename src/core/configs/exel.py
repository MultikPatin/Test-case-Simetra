from pydantic.fields import Field
from pydantic_settings import BaseSettings
from pydantic_settings.main import SettingsConfigDict


class ExelSettings(BaseSettings):
    """
    This class is used to store the Postgres connection settings.
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    filepath: str = Field(default=..., alias="EXEL_FILEPATH")
    buffer_size: str = Field(default=..., alias="EXEL_BUFFERED_ROWS")


settings = ExelSettings()
