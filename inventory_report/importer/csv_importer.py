from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if (path.endswith('.csv')):
            with open(path, "r") as file:
                dictionaty = csv.DictReader(file)
                return [row for row in dictionaty]
        else:
            raise ValueError('Arquivo inválido')
