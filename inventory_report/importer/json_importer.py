import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path_document):
        if not (path_document.endswith(".json")):
            raise ValueError("Arquivo inválido")
        with open(path_document) as f:
            file_in_dict = json.load(f)
        return file_in_dict
