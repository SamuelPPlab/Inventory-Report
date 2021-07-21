from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(cls, path):
        if path.endswith('.json'):
            with open(path) as file:
                return (json.load(file))
        else:
            raise ValueError("Invalid data")
