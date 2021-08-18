import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".csv" in path:
            with open(path, mode="r") as data:
                products = []

                csvFile = csv.DictReader(
                    data, delimiter=",", quotechar='"'
                )

                for data in csvFile:
                    products.append(data)

                return products
        else:
            raise ValueError("Arquivo inválido")
