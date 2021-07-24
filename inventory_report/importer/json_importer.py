from .importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file_path):
        if (file_path[len(file_path) - 5:] != '.json'):
            raise ValueError('Arquivo inválido')
        with open(file_path) as file:
            return json.load(file)
