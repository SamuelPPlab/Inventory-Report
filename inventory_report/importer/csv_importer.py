import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(file):
        if file.endswith(".csv"):
            with open(file, mode="r") as csv_content:
                return list(csv.DictReader(csv_content))

        raise ValueError("Arquivo inválido")
