from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        with open(path, mode="r") as file:
            if path.split(".")[1] == "csv":
                file_reader = csv.DictReader(file)
                return list(file_reader)
            else:
                raise ValueError("Arquivo inválido")
