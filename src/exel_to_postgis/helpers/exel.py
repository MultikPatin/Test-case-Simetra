from collections.abc import Generator

from openpyxl import load_workbook

from src.core.utils.logger import create_logger


class ExelExtractor:
    def __init__(self, filepath: str, buffer_size: int):
        self.__buffer_size = buffer_size
        self.__wb = load_workbook(filepath)
        self.logger = create_logger("SQLiteExtractor")

    def extract(self) -> Generator:
        ws = self.__wb.active
        yield from ws.iter_rows(max_row=ws.max_row, max_col=6)
