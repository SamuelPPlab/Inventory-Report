import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".json" in path:
            products = []

            with open(path, mode="r") as data:
                jsonFile = json.load(data)

            for item in jsonFile:
                products.append(item)

            return products
        else:
            raise ValueError("Arquivo inválido")
