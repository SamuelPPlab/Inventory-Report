from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path_name):
        if ".json" in path_name:
            with open(path_name) as json_file:
                json_reader = json_file.read()
                return json.loads(json_reader)
        raise ValueError("Arquivo inválido")
