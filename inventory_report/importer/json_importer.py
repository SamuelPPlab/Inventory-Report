from inventory_report.importer.importer import Importer
import json


class Json(Importer):

    def import_data(path):
        with open(path) as arquivo:
            arquivoJSON = json.load(arquivo)
            return arquivoJSON
