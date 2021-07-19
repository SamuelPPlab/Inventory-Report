import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def read_json(path):
        with open(path, "r") as file:
            return json.load(file)

    @staticmethod
    def import_data(path):
        file_format = path.split(".")[-1]

        if file_format != "json":
            raise ValueError("Arquivo inválido")

        return JsonImporter.read_json(path)
