from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file):
        if file.endswith("json"):
            with open(file) as file:
                reader = json.load(file)
                return reader
        else:
            raise ValueError("Arquivo inválido")
