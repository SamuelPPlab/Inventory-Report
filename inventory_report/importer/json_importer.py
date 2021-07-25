import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(self, file_path: str) -> dict:
        if file_path.endswith(".json"):
            with open(file_path, mode="r") as file:
                return json.load(file)
        raise ValueError("Arquivo inválido")
