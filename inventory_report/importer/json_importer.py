from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        file_type = cls.check_file_type_in_path(path)
        if file_type == "json":
            with open(path, 'r') as jsonfile:
                data = jsonfile.read()
                reader = json.loads(data)
        else:
            raise ValueError("Arquivo inválido")
        return reader

    @staticmethod
    def check_file_type_in_path(path):
        return path.split(".")[1]
