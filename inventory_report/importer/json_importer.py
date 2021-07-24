import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        try:
            if not path.endswith('.json'):
                raise ValueError('Arquivo inválido')
            with open(path) as file:
                data_report = file.read()
                data = json.loads(data_report)
                return data
        except FileNotFoundError:
            raise ValueError('Arquivo não encontrado')