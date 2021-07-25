import csv
from .importer import Importer


class CsvImporter(Importer):
    def import_data(file_path: str) -> list:
        if file_path.endswith(".csv"):
            with open(file_path, mode="r") as file:
                print(file)
                print(list(csv.DictReader(file)))
                return list(csv.DictReader(file))
        raise ValueError("Arquivo inválido")
