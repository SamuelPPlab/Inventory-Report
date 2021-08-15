import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(file_name):
        if file_name.endswith(".json"):
            with open(file_name) as file:
                read = json.load(file)
                dict = list(read)
                return dict
        else:
            raise ValueError("Arquivo inválido")
