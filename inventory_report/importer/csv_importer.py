from inventory_report.importer.importer import Importer
import csv


class readCSV(Importer):

    def import_data(path):
        with open(path) as arquivo:
            arquivoCSV = csv.DictReader(arquivo)
            return list(arquivoCSV)
