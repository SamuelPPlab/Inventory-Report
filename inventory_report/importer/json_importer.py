from inventory_report.importer.importer import FileExtension, Importer

import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_name: str):
        file_extension: str = Importer.get_file_extension(file_name)

        if file_extension != FileExtension.JSON.value:
            raise ValueError("Arquivo inválido")

        with open(file_name, "r") as file:
            return json.load(file)
