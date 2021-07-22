from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith("csv"):
            raise ValueError("Arquivo inválido")
        with open(path, mode="r") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            list_products = [row for row in content]
            return list_products


if __name__ == "__main__":
    CsvImporter.import_data("inventory_report/data/inventory.csv")
