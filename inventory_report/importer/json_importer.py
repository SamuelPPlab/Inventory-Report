from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        with open(path, mode="r") as file:
            if path.split(".")[1] == "json":
                list = json.load(file)
                return list
            else:
                raise ValueError("Arquivo inválido")
