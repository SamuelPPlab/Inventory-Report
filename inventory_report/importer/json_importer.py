import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not (file_path.endswith(".json")):
            raise ValueError("Arquivo inválido")
        with open(file_path) as fd:
            dict_products = json.load(fd)
        return dict_products
