import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    def import_data(file_name):
        if file_name.endswith(".csv"):
            with open(file_name) as file:
                read = csv.DictReader(file)
                dict = list(read)
                return dict
        else:
            raise ValueError("Arquivo inválido")
