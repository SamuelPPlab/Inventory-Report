from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        with open(path, 'r') as json_file:
            if path.endswith("json"):
                json_list = json.load(json_file)
                return json_list
            else:
                raise ValueError('Arquivo inválido')
