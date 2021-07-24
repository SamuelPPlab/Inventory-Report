from .importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file_path):
        if (file_path[len(file_path) - 4:] != '.csv'):
            raise ValueError('Arquivo inválido')

        with open(file_path) as file:
            read_file = csv.DictReader(file)
            return [item for item in read_file]
