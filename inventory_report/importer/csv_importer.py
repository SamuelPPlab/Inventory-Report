from inventory_report.importer.importer import Importer
from csv import DictReader


class CsvImporter(Importer):
    def import_data(path):
        data = []
        with open(path, mode="r") as csv_file:
            if not path.endswith("csv"):
                raise ValueError("Arquivo inválido")
            reader_csv = DictReader(csv_file)
            data = [rows for rows in reader_csv]
            return data
