from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    @classmethod
    def import_data(path):
        with open(path) as file:
            return json.load(file)
