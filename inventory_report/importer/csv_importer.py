from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def __init__(self):
        print("Csv Importer")

    @staticmethod
    def import_data(file):
        isTrue = file.endswith(".csv")
        if isTrue:
            with open(file) as file:
                csv_file = csv.DictReader(file, delimiter=",")
                inventory = [row for row in csv_file]
            return inventory
        else:
            raise ValueError("Arquivo inválido")
