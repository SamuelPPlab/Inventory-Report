from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def __init__(self):
        print("Json Importer")

    @staticmethod
    def import_data(file):
        isTrue = file.endswith(".json")
        if isTrue:
            with open(file) as file:
                json_file = json.load(file)
            return list(json_file)
        else:
            raise ValueError("Arquivo inválido")
