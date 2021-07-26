import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if file_name.split('.')[1] != 'json':
            raise ValueError('Arquivo inválido')

        with open(file_name) as file:
            file_read = file.read()
            data = json.loads(file_read)
            return data
