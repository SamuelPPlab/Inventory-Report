import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not (file_path.endswith(".csv")):
            raise ValueError("Arquivo inválido")
        with open(file_path) as fd:
            dict_products = [row for row in csv.DictReader(fd)]
        return dict_products
