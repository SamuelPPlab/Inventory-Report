from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_type = cls.check_file_type_in_path(path)
        if file_type == "csv":
            with open(path, newline="") as csvfile:
                reader = list(csv.DictReader(csvfile))
        else:
            raise ValueError("Arquivo inválido")
        return reader

    @staticmethod
    def check_file_type_in_path(path):
        return path.split(".")[1]
