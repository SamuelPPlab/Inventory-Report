from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(cls, path):
        if path.endswith(".csv"):
            with open(path) as file:
                return list(csv.DictReader(file))
        else:
            raise ValueError("Invalid data")
