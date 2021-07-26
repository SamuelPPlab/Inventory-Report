from .importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if path.split(".")[1] == "csv":
            with open(path, mode="r") as arquivo:
                reader = csv.DictReader(arquivo)
                lista = []
                for linha in reader:
                    lista.append(linha)
            return lista
        else:
            raise ValueError("Arquivo inválido")
