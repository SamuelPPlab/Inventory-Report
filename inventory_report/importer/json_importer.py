import json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(file_path: str) -> dict:
        if file_path.endswith(".json"):
            with open(file_path, mode="r") as file:
                return json.load(file)
        raise ValueError("Arquivo inválido")
