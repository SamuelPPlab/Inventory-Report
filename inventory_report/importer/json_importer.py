from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file):
        if not file.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(file) as file_json:
            inventory = json.load(file_json)
            result = inventory
        return result
