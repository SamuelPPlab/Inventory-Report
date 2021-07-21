from inventory_report.importer.importer import Importer
import pathlib
from csv import DictReader


class CsvImporter(Importer):
    def import_data(file):
        data = []
        with open(file, mode="r") as csv_file:
            if pathlib.Path(csv_file.name).suffix != "csv":
                raise ValueError("Arquivo inválido")
            reader_csv = DictReader(csv_file)
            for rows in reader_csv:
                data.append(rows)     

            return data
