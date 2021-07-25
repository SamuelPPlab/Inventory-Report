import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(file_name):
        with open(file_name, 'r') as content_file:
            if file_name.endswith(".csv"):
                csv_importer = csv.DictReader(content_file)
                return list(csv_importer)
            else:
                raise ValueError("Arquivo inválido")
