from inventory_report.importer.importer import Importer
import pathlib
import json


class JsonImporter(Importer):
    def import_data(file):
        data = []
        with open(file, mode="r") as json_file:
            if pathlib.Path(json_file.name).suffix != "json":
                raise ValueError("Arquivo inválido")
            data = json.load(json_file)          

        return data
