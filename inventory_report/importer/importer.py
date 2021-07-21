from enum import Enum
from abc import ABC, abstractmethod


class FileExtension(Enum):
    JSON = "json"
    CSV = "csv"
    XML = "xml"


class Importer(ABC):
    @staticmethod
    def get_file_extension(file_name: str):
        return file_name.split(".")[-1]

    @abstractmethod
    def import_data(file_name: str):
        raise NotImplementedError
