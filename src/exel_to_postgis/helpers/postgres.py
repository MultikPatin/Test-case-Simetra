from collections.abc import Generator
from dataclasses import fields

from psycopg2.extensions import connection as _connection

from src.core.utils.logger import create_logger
from src.exel_to_postgis.schemas.exel import ExelRow


class PostgresSaver:
    __cursor = None

    def __init__(self, connection: _connection):
        self.__connection = connection
        self.logger = create_logger("PostgresSaver")

    def save(self, rows: Generator):
        self.__cursor = self.__connection.cursor()
        self.__truncate_tables()  # реализовано для разработки
        self.__save_table(rows)
        self.logger.debug("Завершено копирование данных для таблицы")
        self.__cursor.close()

    #
    def __truncate_tables(self):
        stmt = "TRUNCATE vehicles CASCADE"
        self.__cursor.execute(stmt)
        self.logger.debug(stmt)

    def __save_table(self, generator: Generator):
        for rows in generator:
            values = self.__get_insert_values(rows)
            column = self.__get_column_names_str()
            self.__insert_data(column, values)

    def __insert_data(self, column: str, values: str):
        stmt = (
            f"INSERT INTO vehicles ({column}) VALUES {values} "
            f" ON CONFLICT (id) DO NOTHING"
        )

        self.__cursor.execute(stmt)

    @staticmethod
    def __get_column_names_str() -> str:
        column_names = [field.name for field in fields(ExelRow)]
        column_names.remove("longitude")
        column_names.remove("latitude")
        column_names.append("geom")
        column_names_str = ",".join(column_names)
        return column_names_str

    def __get_insert_values(self, rows: list[ExelRow]) -> str:
        values = [
            (
                row.id,
                row.speed,
                row.gps_time,
                row.vehicle_id,
                row.get_point,
            )
            for row in rows
        ]
        values = ", ".join(
            str(self.__validate_value(value)) for value in values
        )
        return values

    @staticmethod
    def __validate_value(row):
        # TODO: реализовать валидацию строки таблицы
        return row
