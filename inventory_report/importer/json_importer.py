from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(arq):
        with open(arq, "r") as content:
            result = json.load(content)
            return result
