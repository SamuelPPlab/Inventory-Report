from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        return json.load(open(path))
