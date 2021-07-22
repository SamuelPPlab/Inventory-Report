from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):

    def import_data(file_name):
        if file_name.count('json') != 0:
            with open(file_name) as file:
                result = json.load(file)
                return result
        else:
            raise ValueError('Arquivo inválido')
