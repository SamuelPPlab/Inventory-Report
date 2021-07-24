import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(file_path: str) -> list:
        if file_path.endswith(".csv"):
            with open(file_path, mode="r") as file:
                return list(csv.DictReader(file))
        raise ValueError("Arquivo inválido")
