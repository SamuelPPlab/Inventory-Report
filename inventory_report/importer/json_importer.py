from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file_path):
        if file_path.endswith("json"):
            with open(file_path, 'r') as json_file:
                content = json.load(json_file)
                return content
        else:
            raise ValueError("Arquivo inválido")
