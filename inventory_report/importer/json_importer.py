from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file):
        data = []
        with open(file, mode="r") as json_file:
            if not file.endswith("json"):
                raise ValueError("Arquivo inválido")
            data = json.load(json_file)

        return data
