from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file):
        if not file.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(file) as file_csv:
            inventory = csv.DictReader(file_csv)
            result = list(inventory)
        return result

# easteregg