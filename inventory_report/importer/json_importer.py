from .importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        if path.split(".")[1] == "json":
            with open(path, mode="r") as arquivo:
                lista = json.load(arquivo)
            return lista
        else:
            raise ValueError("Arquivo inválido")
