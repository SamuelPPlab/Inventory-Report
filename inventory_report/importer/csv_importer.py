import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def read_csv(path):
        with open(path) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            header, *rows = reader

            return [dict(zip(header, row)) for row in rows]

    @staticmethod
    def import_data(path):
        file_format = path.split(".")[-1]

        if file_format != "csv":
            raise ValueError("Arquivo inválido'")

        return CsvImporter.read_csv(path)
