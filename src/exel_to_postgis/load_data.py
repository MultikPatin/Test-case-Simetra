from pathlib import Path

import psycopg2
from psycopg2.extensions import connection
from psycopg2.extras import DictCursor

from src.core.configs import exel_settings, postgres_settings
from src.exel_to_postgis.helpers.exel import ExelExtractor
from src.exel_to_postgis.helpers.postgres import PostgresSaver

DSN = {
    "dbname": postgres_settings.db_name,
    "user": postgres_settings.user,
    "password": postgres_settings.password.get_secret_value(),
    "host": postgres_settings.host,
    "port": postgres_settings.port,
    "cursor_factory": DictCursor,
}

script_dir = Path(__file__).parent.resolve()
exel_filepath = str(script_dir) + exel_settings.filepath


def load_from_exel(filepath: str, postgres_conn: connection, buffer_size: int):
    """Основной метод загрузки данных из Exel в Postgres"""
    postgres_saver = PostgresSaver(postgres_conn)
    exel_extractor = ExelExtractor(filepath, buffer_size)

    rows = exel_extractor.extract()
    postgres_saver.save(rows)


if __name__ == "__main__":
    with psycopg2.connect(**DSN) as pg_conn:
        load_from_exel(exel_filepath, pg_conn, exel_settings.buffer_size)
