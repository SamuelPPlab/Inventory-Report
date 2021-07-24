import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path_document):
        if not (path_document.endswith(".csv")):
            raise ValueError("Arquivo inválido")
        with open(path_document) as f:
            file_in_dict = [row for row in csv.DictReader(f)]
        return file_in_dict
