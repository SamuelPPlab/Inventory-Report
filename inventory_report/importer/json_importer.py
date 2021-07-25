from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            content = file.read()
            inventory_data = json.loads(content)
            return list(inventory_data)
