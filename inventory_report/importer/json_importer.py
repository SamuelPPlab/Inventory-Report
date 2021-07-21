import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(file):
        if file.endswith(".json"):
            with open(file, mode="r") as json_content:
                return json.load(json_content)

        raise ValueError("Arquivo inválido")
