from inventory_report.importer.importer import Importer
import pathlib
from csv import DictReader


class CsvImporter(Importer):
    def import_data(file_to_read):
        data = []
        with open(file_to_read, 'r') as file:
            if pathlib.Path(file.name).suffix != '.csv':
                raise ValueError("Arquivo inválido")
            csvReader = DictReader(file)
            for rows in csvReader:
                data.append(rows)
        return data
