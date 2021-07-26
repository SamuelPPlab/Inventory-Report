from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        with open(path, 'r') as csv_file:
            if path.endswith("csv"):
                csv_list = csv.DictReader(csv_file)
                return list(csv_list)
            else:
                raise ValueError('Arquivo inválido')
