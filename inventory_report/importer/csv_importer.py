from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file):
        if file.endswith("csv"):
            with open(file) as file:
                reader = list(csv.DictReader(file))
                return reader
        else:
            raise ValueError("Arquivo inválido")
