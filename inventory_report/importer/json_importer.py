import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(file_name):
        with open(file_name, 'r') as content_file:
            if file_name.endswith(".json"):
                return json.load(content_file)
            else:
                raise ValueError("Arquivo inválido")
