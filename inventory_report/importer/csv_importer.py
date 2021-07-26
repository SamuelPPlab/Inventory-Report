from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):

    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path) as arquivo:
            arquivoCSV = csv.DictReader(arquivo)
            return list(arquivoCSV)
