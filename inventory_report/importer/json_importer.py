from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    @classmethod
    def import_data(path):
        if (path.endswith('.json')):
            with open(path) as file:
                return json.load(file)
        else:
            raise Exception('Arquivo incorreto')
