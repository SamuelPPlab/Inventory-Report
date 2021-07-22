import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(path, newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(data for data in reader)

        return data
