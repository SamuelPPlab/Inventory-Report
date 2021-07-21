from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file_path):
        file_extension = file_path.split(".")[1]
        try:
            if file_extension == 'json':
                with open(file_path, 'r') as json_file:
                    inv_report = json.load(json_file)
                return inv_report
            else:
                raise ValueError('Arquivo inválido')
        except ValueError:
            print('Arquivo inválido')
            raise
