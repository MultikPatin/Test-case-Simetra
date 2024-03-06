from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))

from .exel import settings as exel_settings  # noqa
from .postgres import settings as postgres_settings  # noqa
