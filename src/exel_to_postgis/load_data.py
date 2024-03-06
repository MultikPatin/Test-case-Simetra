# import psycopg2
# from psycopg2.extensions import connection
#
# from src.core.configs import exel_settings, postgres_settings
# from src.exel_to_postgis.helpers.exel import ExelExtractor
# from src.exel_to_postgis.helpers.postgres import PostgresSaver
#
#
# def load_from_exel(
#     exel_filepath: str, postgres_conn: connection, buffer_size: int
# ):
#     """Основной метод загрузки данных из Exel в Postgres"""
#     postgres_saver = PostgresSaver(postgres_conn)
#     exel_extractor = ExelExtractor(exel_filepath, buffer_size)
#
#     rows = exel_extractor.extract()
#     postgres_saver.save(rows)
#
#
# if __name__ == "__main__":
#     with psycopg2.connect(
#         **postgres_settings.psycopg2_connect_local
#     ) as pg_conn:
#         load_from_exel(
#             exel_settings.filepath, pg_conn, exel_settings.buffer_size
#         )
