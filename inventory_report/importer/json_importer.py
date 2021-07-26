from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path) as arquivo:
            arquivoJSON = json.load(arquivo)
            return arquivoJSON
