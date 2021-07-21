import json
import pathlib
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(file_to_read):
        data = []
        with open(file_to_read, 'r') as file:
            if pathlib.Path(file.name).suffix != '.json':
                raise ValueError("Arquivo inválido")
            data = json.load(file)
        return data
