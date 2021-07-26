from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if path.endswith('.json'):
            with open(path, mode='r') as file:
                return json.load(file)

        raise ValueError("Arquivo inválido")
